import os
import joblib
import pandas as pd


def load_model(model_path):
    """
    Load a machine learning model from the specified path.

    Parameters:
    model_path (str): Path to the model file.

    Returns:
    model: Loaded machine learning model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = joblib.load(model_path)
    return model


def generate_predictions(model, test_data):
    """
    Generate predictions using the loaded model on the test data.

    Parameters:
    model: Loaded machine learning model.
    test_data (pd.DataFrame): Test data for predictions.

    Returns:
    pd.Series: Predictions for the test data.
    """
    predictions = model.predict(test_data)
    return pd.Series(predictions)


if __name__ == "__main__":
    model = load_model("models/best_model.joblib")
    data_to_predict = pd.read_parquet("data/test.parquet")
    x_test = data_to_predict.drop("quality", axis=1)
    predictions = generate_predictions(model, x_test)
    print(predictions)
