from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientPrototipy(BaseModel):
    name: str
    email: EmailStr
    age: int
    description: Optional[str] = None

class Client(ClientPrototipy):
    id: int = Field(default=None)

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

