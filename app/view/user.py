from datetime import datetime

from fastapi import APIRouter

from app.model.user import user_info
from app.schema.user import UserScoreItem

router = APIRouter()


@router.post("/role/score:calculate")
async def add_score_endpoint(req: UserScoreItem):
    user = user_info.get_user(user_id := req.user_id)
    role_func = {
        "staff": cal_staff_score,
        "admin": cal_staff_score,
    }
    if req.score:
        user["score"] += role_func.get(req.role)[req]
    user["last_login"] = datetime.now()
    user_info.update_user(user_id, user)
    return user.dict()


def cal_staff_score(body):
    return body["score"]


def cal_admin_score(body):
    return body["score"] * body["score_modifier"]
