from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
    prefix="/account",
    tags=["accounts"]
)

@router.post("/", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(database.get_db)):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.get("/{id}", response_model=schemas.Account)
def get_account(id: int, db: Session = Depends(database.get_db)):
    account = db.query(models.Account).filter(models.Account.id == id).first()
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account
