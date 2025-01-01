"""Script for data preparation."""

import sys
from pathlib import Path

import pandas as pd
from loguru import logger
from sklearn import model_selection
import yaml

# Load configuration
with Path("config/config.yaml").open() as file:
    config = yaml.safe_load(file)


def prepare_data(config) -> None:
    """Prepare train and test raw red wine data.

    :param config_path: Path to configuration file.
    :param in_path: Path where raw data is read from.
    :param out_train: Path where prepared train data is stored.
    :param out_test: Path where prepared test data is stored.
    """
    try:
        logger.info("Cleaning data")

        data = pd.read_csv(config["data"]["data_dir"] + "/winequality-red.csv")
        logger.info(
            "Raw data read from {} file",
        )

        train, test = model_selection.train_test_split(
            data, test_size=config["data"]["test_size"], random_state=config["data"]["random_state"]
        )
        logger.debug("Train and test data split")

        train.to_parquet(config["data"]["data_dir"] + "/train.parquet")
        logger.info("Train data saved to {} file", config["data"]["data_dir"] + "/train.parquet")

        test.to_parquet(config["data"]["data_dir"] + "/test.parquet")
        logger.info("Test data saved to {} file", config["data"]["data_dir"] + "/test.parquet")

    except Exception as exc:
        logger.error("Unexpected error")
        logger.error(exc.with_traceback())
        sys.exit(1)


if __name__ == "__main__":
    prepare_data(config=config)
