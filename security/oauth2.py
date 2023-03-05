from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from schemas import TokenData
from utils import Constants as consts

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=consts.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, consts.SECRET_KEY, algorithm=consts.ALGORITHM)

    return encoded_jwt

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
    
def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Couldn't validate Credentials!", headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token, credentials_exception)