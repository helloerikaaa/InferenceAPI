import os
from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.services.models import PenguinsModel


def _startup_model(app: FastAPI) -> None:
    """
    Method to start a new instance of the model

    Parameters:
        app (FastAPI): The FastAPI instance of the application
    """
    model_instance = PenguinsModel()
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    """
    Method to delete a model instance

    Parameters:
        app (FastAPI): The FastAPI instance of the application
    """
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    """
    Callable to start the model instance handler

    Parameters:
        app (FastAPI): The FastAPI instance of the application

    Returns:
        Callable to start the model instance
    """

    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    """
    Callable to end the model instance handler

    Parameters:
        app (FastAPI): The FastAPI instance of the application

    Returns:
        Callable to end the model instance
    """

    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
