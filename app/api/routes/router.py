from fastapi import APIRouter

from app.api.routes import heartbeat, predict

api_router = APIRouter()

api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(predict.router, tags=["predict"], prefix="/predict")
