import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 3))


class ModelPaths:
    artifacts = os.path.join(PROJECT_PATH, "artifacts")
