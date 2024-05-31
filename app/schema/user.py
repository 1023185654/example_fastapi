from pydantic import BaseModel


class UserScoreItem(BaseModel):
    user_id: str
    role: str
    score: int = 0
    score_modifier: int = 0
