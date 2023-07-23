from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from schemas import TokenData
from utils import Constants as consts
from models import User
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(user):
    payload = {
        "id": user.id,
        "exp": datetime.utcnow() + timedelta(days=consts.ACCESS_TOKEN_EXPIRE_DAYS),
    }
    token = jwt.encode(payload, consts.SECRET_KEY, algorithm=consts.ALGORITHM)
    return token


def decode_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, consts.SECRET_KEY, algorithms=[consts.ALGORITHM])
        id: int = payload.get("id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)

    except JWTError:
        raise credentials_exception

    return token_data


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return decode_token(token, credentials_exception)


async def get_user(db: Session, id: int) -> User:
    return db.query(User).filter_by(id=id).first()
