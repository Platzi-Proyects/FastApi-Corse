from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import SQLModel, Field

class ClientPrototipy(SQLModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)
    description: Optional[str] = None

class Client(ClientPrototipy, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ClientUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    description: Optional[str] = None



class Sale(BaseModel):
    id: int
    amount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: Client
    sales: list[Sale]
    total: int

    @property
    def amount_total(self):
        return sum(sale.amount for sale in self.sales)

