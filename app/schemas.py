from pydantic import BaseModel
from typing import List, Optional

class AccountCreate(BaseModel):
    account_type: str
    name: str
    document: str

class Account(BaseModel):
    id: int
    account_type: str
    name: str
    document: str
    balance: float

    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    amount: float
    transaction_type: str
    account_id: int

class Transaction(BaseModel):
    id: int
    amount: float
    transaction_type: str
    account_id: int

    class Config:
        orm_mode = True
