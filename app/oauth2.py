from jose import JWTError, jwt
from datetime import datetime, timedelta
from .schemas import TokenData
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from .database import get_db
from sqlalchemy.orm import Session
from .models import User
from .config import setting

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#SECRET_KEY
#ALGORITHM
#EXPIRATION_TIME

SECRET_KEY = f"{setting.secret_key}"
ALGORITHM = f"{setting.algorithm}"
ACCESS_TOKEN_EXPIRE_MINUTES = setting.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verfiy_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        
        token_data = TokenData(id=id)
    
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate Credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token = verfiy_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token.id).first()

    return user