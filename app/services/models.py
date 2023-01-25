from typing import List

import os
import json
import numpy as np
import pandas as pd
from loguru import logger

from app.consts.paths import ModelPaths
from app.models.metadata import MetadataResult
from app.models.prediction import PredictionResult
from app.services.load_model import _load_local_model
from app.models.payload import Payload, payload_to_list


class PenguinsModel(object):
    def __init__(self):
        self.model = _load_local_model(os.path.join(ModelPaths.artifacts, "model.pkl"))
        self.meta = os.path.join(ModelPaths.artifacts, "metadata.json")

    def _pre_process(self, payload: Payload) -> List:
        logger.info("Pre-processing payload")
        logger.info(f"Payload: {payload}")

        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        logger.info(result)
        return result

    def _post_process(self, prediction: np.ndarray) -> PredictionResult:
        logger.info("Post processing prediction")

        with open(self.meta) as f:
            metadata = json.load(f)

        meta = json.loads(metadata)

        model_metadata = MetadataResult(
            algorithm_name=meta["algorithm"],
            model_name=meta["model_name"],
            version=meta["version"],
            metrics=meta["metrics"],
        )

        prediction = PredictionResult(
            success=True,
            probability=prediction,
            metadata=model_metadata,
            message="Prediction success",
        )

        return prediction

    def _predict(self, features: List) -> np.ndarray:
        logger.info("Predicting sex of penguins...")
        prediction_result = self.model.predict_proba(features)
        logger.info(f"Prediction of the two classes {prediction_result}")

        return prediction_result.tolist()[0][1]

    def predict(self, payload: Payload):

        pre_processed_payload = self._pre_process(payload)
        logger.info(f"Preproccesed payload {pre_processed_payload}")

        prediction = self._predict(pre_processed_payload)
        logger.info(f"Prediction: {prediction}")

        post_processed_result = self._post_process(prediction)
        logger.info(f"Post processed result: {post_processed_result}")

        return post_processed_result
