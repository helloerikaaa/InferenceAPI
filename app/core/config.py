from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

# application metadata settings
APP_VERSION: str = config("APP_VERSION")
APP_NAME: str = config("APP_NAME")
API_PREFIX: str = "/api"

# security settings
API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
