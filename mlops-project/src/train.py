"""Implements the training pipeline for regression models.

It loads data, performs grid search for hyperparameter tuning, and saves the best
performing model.
"""

from pathlib import Path

import joblib
import pandas as pd
import yaml
from catboost import CatBoostRegressor
from loguru import logger
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import mlflow

# Load configuration
with Path("config/config.yaml").open() as file:
    config = yaml.safe_load(file)


def train_model() -> None:
    """Trains regression models using grid search for hyperparameter tuning, evaluates the best
    model on the test set, and saves the best model."""
    # Load data
    train_data = pd.read_parquet("data/train.parquet")
    test_data = pd.read_parquet("data/test.parquet")

    # Separate features and target
    x_train = train_data.drop(
        config["target"], axis=1
    )  # Replace 'target' with your target column name
    y_train = train_data[config["target"]]
    x_test = test_data.drop(config["target"], axis=1)
    y_test = test_data[config["target"]]

    # Define models and their parameter grids
    models = {
        "RandomForest": {
            "model": RandomForestRegressor(random_state=42),
            "params": config["rf_hp"],
        },
        "CatBoost": {
            "model": CatBoostRegressor(random_state=42, verbose=False),
            "params": config["lgbm_hp"],
        },
    }

    # Dictionary to store results
    results = {}

    # Perform GridSearch for each model
    for name, model_info in models.items():
        grid_search = GridSearchCV(
            estimator=model_info["model"],
            param_grid=model_info["params"],
            cv=5,
            scoring="neg_mean_squared_error",
            n_jobs=-1,
        )

        grid_search.fit(x_train, y_train)

        # Store results
        results[name] = {
            "best_params": grid_search.best_params_,
            "best_score": -grid_search.best_score_,  # Convert back to MSE
            "best_model": grid_search.best_estimator_,
        }

        logger.info("{} best MSE: {}", name, grid_search.best_score_)
        logger.info("{} best parameters: {}", name, grid_search.best_params_)
        # Log best score and parameters to MLflow
        mlflow.log_metric(f"{name}_best_mse", -grid_search.best_score_)
        mlflow.log_params(
            {f"{name}_{key}": value for key, value in grid_search.best_params_.items()}
        )

    # Select the best model
    best_model_name = min(results.items(), key=lambda x: x[1]["best_score"])[0]
    best_model = results[best_model_name]["best_model"]

    # Evaluate best model on test set
    y_pred = best_model.predict(x_test)
    test_mse = mean_squared_error(y_test, y_pred)
    test_r2 = r2_score(y_test, y_pred)

    logger.info("\nBest Model Results:")
    logger.info("Best Model: {}", best_model_name)
    logger.info("Test MSE: {}", test_mse)
    logger.info("Test R2: {}", test_r2)
    # Log test metrics to MLflow
    mlflow.log_metric("test_mse", test_mse)
    mlflow.log_metric("test_r2", test_r2)

    # Save the best model
    joblib.dump(best_model, "models/best_model.joblib")
    logger.info("\nBest model saved as 'models/best_model.joblib'")
    # Log the best model as an MLflow artifact
    mlflow.sklearn.log_model(best_model, "best_model")
    logger.info("Best model logged as an MLflow artifact")


if __name__ == "__main__":
    mlflow.set_experiment("wine-quality")

    with mlflow.start_run():
        train_model()
