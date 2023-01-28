import os
import pickle
from loguru import logger


def load_local_model(path: str):
    try:
        model = pickle.load(open(path, "rb"))
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Error loading model {e}")
    
    return model
