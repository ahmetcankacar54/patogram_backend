from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from schemas import TokenData
from utils import Constants as consts
from models import User
from database.configuration import get_db
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=consts.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, consts.SECRET_KEY, algorithm=consts.ALGORITHM)

    return encoded_jwt

"""def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, consts.SECRET_KEY, algorithms=[consts.ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            return {"Uyari": "Burasi Yarra Yedi"}
        token_data = TokenData(id=id)
    except JWTError:
        return {"Uyari": "Burasi Saglam Yarra Yedi"}

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user = db.query(User).filter(User.id == token).first()

    return user




def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, consts.SECRET_KEY, algorithms=[consts.ALGORITHM])
        id: str = payload.get("user_id")
        
        if id is None:
            raise credentials_exception
        
        token_data = TokenData(id= id)
    except JWTError:
        raise credentials_exception
    return token_data
    
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    # token = verify_access_token(token, credentials_exception)
    payload = jwt.decode(token, consts.SECRET_KEY, algorithms=[consts.ALGORITHM])
    user = await get_user(db, payload["id"])
    # user = db.query(User).filter(User.id == token.id).first()
    print(user)

    return TokenData(user)"""

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, consts.SECRET_KEY, algorithms=[consts.ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id= user_id)
        print(token_data)
    except JWTError:
        raise credentials_exception
    #user = get_user(get_db, id=token_data.id)
    #if user is None:
     #   raise credentials_exception
    return token_data

async def get_user(db: Session, id: int) -> User:
    return db.query(User).filter_by(id=id).first()
