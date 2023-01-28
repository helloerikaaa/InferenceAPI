from fastapi import APIRouter

from app.models.heartbeat import HeartbeatResult

router = APIRouter()


@router.get("/heartbeat", response_model=HeartbeatResult, name="heartbeat")
def get_hearbeat() -> HeartbeatResult:
    heartbeat = HeartbeatResult(is_alive=True)
    return heartbeat
