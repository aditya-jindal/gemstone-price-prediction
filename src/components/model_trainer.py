import os
import sys
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
from src.exception.exception import MyException
from src.logger.logging import logging
from src.utils.utils import save_object

class ModelTrainerConfig:
    model_filepath = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def generate_perf_report(self, X_train, y_train, models):
        try:
            logging.info("Fitting models to train data.")
            perf_report = {}
            for model_name, model_object in models.items():
                y_pred = model_object.fit(X_train)
                perf_report[model_name] = r2_score(y_pred, y_train)
            logging.info("Models fitting done.")

            return perf_report
    
        except Exception as e:
            logging.info("Encountered exception while fitting model to train data.")
            raise MyException(e, sys)

            return None

    def initiate_model_training(self, train_data, test_data):
        try:
            logging.info("Splitting features and target from train and test data.")
            X_train, y_train, X_test, y_test = (train_data[:, :-1], train_data[:, -1], test_data[:, :-1], test_data[:, -1])
            logging.info("Obtained split training and test data.")
            
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'RandomForest': RandomForestRegressor(),
                'XGBoost': XGBRegressor()
            }

            perf_report = self.generate_perf_report(X_train, y_train, models)
            logging.info("Model Performance Report Generated:-")
            logging.info(perf_report)
            
            best_model_name = max(perf_report, key=perf_report.get)
            best_model_object = models[best_model_name]
            logging.info(f"Best model found to be {best_model_name} with R2 score of {perf_report[best_model_name]}")

            save_object(self.config.model_filepath, best_model_object)


        except Exception as e:
            logging.info("Encountered exception while model training.")
            raise MyException(e, sys)
            return None