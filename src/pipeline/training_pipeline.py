import os
import sys
from src.logger.logging import logging
from src.exception.exception import MyException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


data_ingestion_obj = DataIngestion()
train_data_path, test_data_path = data_ingestion_obj.initiate_data_ingestion()

data_transformation_obj = DataTransformation()
train_data, test_data = data_transformation_obj.initiate_data_transformation(train_data_path, test_data_path)

model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_data, test_data)
