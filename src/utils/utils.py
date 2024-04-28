import os
import sys
import pickle
from src.logger.logging import logging
from src.exception.exception import MyException
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def save_object(file_path, obj):
    try:
        logging.info(f"Saving object in directory: {file_path}")
        os.makedirs(os.path.dirnameI(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Object dumped.")

    except Exception as e:
        logging.info("Encountered exception while saving object in utils.save_object().")    
        raise MyException(e, sys)
    
def load_object(file_path):
    try:
        logging.info(f"Loading object at directory: {file_path}")
        with open(file_path,'rb') as file_obj:    
            return pickle.load(file_obj)
        
    except Exception as e:
        logging.info('Encountered exception while loading object in utils.load_object().')
        raise MyException(e,sys)