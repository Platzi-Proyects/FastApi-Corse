# Fist Steps

from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# Date Time Endpoints

# from datetime import datetime
# from zoneinfo import ZoneInfo

# currentTimezone = {
#     "EST": "America/New_York",
#     "PST": "America/Los_Angeles",
#     "GMT": "Europe/London",
#     "UTC": "UTC",
#     "IST": "Asia/Kolkata"
# }

# @app.get("/{iso_str}")
# async def root(iso_str: str):
#     iso = iso_str.upper()
#     timesome_str = currentTimezone.get(iso)
#     tz = ZoneInfo(timesome_str)
#     return {
#         "time": datetime.now(tz).isoformat(),
#     }

from models import Client, Sale, Invoice, ClientPrototipy

db_clients: list[Client] = []

@app.post("/client", response_model=Client)
async def create_user(customerCreate: ClientPrototipy):
    new_id = len(db_clients)
    customer = Client(id=new_id, **customerCreate.model_dump())
    db_clients.append(customer)
    return customer

@app.get("/client", response_model=list[Client])
async def get_clients():
    return db_clients

@app.post("/client/{id}")
async def get_customer_Id(id: int):
    return db_clients[id]


@app.post("/sale")
async def create_sale(sale: Sale):
    return sale

@app.post("/invoice")
async def create_invoice(invoice: Invoice):
    return invoice