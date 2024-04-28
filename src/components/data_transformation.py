import os
import sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from src.exception.exception import MyException
from src.logger.logging import logging
from src.utils.utils import save_object


class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.config = DataTransformationConfig()


    def get_preprocessor_pipeline(self):
        try:
            logging.info("Pipeline initiated.")

            cat_cols = ['cut', 'color','clarity']
            num_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define custom ranking for each ordinal variable
            cut_encoding = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_encoding = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_encoding = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            num_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])
            cat_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="most-frequent")),
                ("ordinal-encoder", OrdinalEncoder([cut_encoding, color_encoding, clarity_encoding]))
                ("scalar", StandardScaler())
            ])
            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, num_cols),
                ("cat_pipeline", cat_pipeline, cat_cols)
            ])
            logging.info("Pipeline created.")

            return preprocessor
        
        except Exception as e:
            logging.info("Encountered exception during pipeline creation.")
            raise MyException(e, sys)
        
            return None

    def initialize_data_transformation(self, train_path, test_path):
        try:
            logging.info("Started data transformation.")

            logging.info("Reading train and test data.")
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info("Loaded train and test data.")

            preprocessor = self.get_preprocessor_pipeline()

            target_col = "price"

            X_train = train_data.drop(["id", target_col], axis=1)
            y_train = train_data[target_col]
            X_test = test_data.drop(["id", target_col], axis=1)
            y_test = test_data[target_col]

            logging.info("Applying preprocessing on train and test data.")
            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)
            train_data = np.concatenate((X_train, y_train), axis=1)
            test_data = np.concatenate((X_test, y_test), axis=1)
            logging.info("Preprocessed train and test data.")

            save_object(self.config.preprocessor_path, preprocessor)
            logging.info("Saved preprocessing object.")

            return train_data, test_data

        except Exception as e:
            logging.info("Encountered exception while data transformation in components.data_transformation")
            raise MyException(e, sys)
        
            return None, None
