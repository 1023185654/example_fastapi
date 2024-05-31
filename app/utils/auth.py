from functools import wraps

from fastapi import HTTPException
from jose import JWTError, jwt

_JWT_SECRET = "your_secret_key"


def authorize_token(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        token = kwargs.get("token_ds")
        if not token:
            raise HTTPException(status_code=401, detail="please login")
        try:
            jwt.decode(token, _JWT_SECRET, algorithms=["HS256"])
        except JWTError:
            raise HTTPException(status_code=401, detail="token not valid")
        return await func(*args, **kwargs)

    return wrapper
