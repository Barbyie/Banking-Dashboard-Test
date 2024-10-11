from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime
from ..database import get_db
from sqlalchemy.orm import Session
from ..models import Account

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

SECRET_KEY = "758603a3-cb1c-4d3f-b4b4-aa8975236894"
ALGORITHM = "HS256"


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        document = payload.get("sub")
        if document is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = db.query(Account).filter(Account.document == document).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
