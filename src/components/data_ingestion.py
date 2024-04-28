import os
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger.logging import logging
from src.exception.exception import MyException
import sys


@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join("data", "train.csv")
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def load_save_raw_data(self):
        os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
        data = pd.read_csv(self.config.raw_data_path)
        data.to_csv(self.config.raw_data_path, index=False)
        return data

    def save_train_data(self, data):
        os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
        data.to_csv(self.config.train_data_path, index=False)

    def save_test_data(self, data):
        os.makedirs(os.path.dirname(self.config.test_data_path), exist_ok=True)
        data.to_csv(self.config.test_data_path, index=False)

    def initiate_data_ingestion(self):
        try:
            logging.info("Initiating data ingestion.")
            raw_data = self.load_save_raw_data()

            logging.info("Splitting data into train and test sets.")
            train_data, test_data = train_test_split(raw_data, test_size=0.2)

            logging.info("Saving train and test data in artifacts.")
            self.save_train_data(train_data)
            self.save_test_data(test_data)

            logging.info("Data ingestion completed.")

            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            logging.error(f"Error in data ingestion: {e}")
            raise MyException(e, sys)

            return None, None

     
if __name__ == "__main__":
    
    obj = DataIngestion()
    obj.initiate_data_ingestion()
