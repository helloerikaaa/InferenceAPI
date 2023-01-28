from pydantic import BaseModel


class MetadataResult(BaseModel):
    algorithm_name: str
    model_name: str
    metrics: dict
