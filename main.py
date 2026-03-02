# Fist Steps

from sqlmodel import select
from fastapi import FastAPI, HTTPException, status
from dbport import SessionDep, create_all_tables

app = FastAPI(lifespan=create_all_tables)



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

from models import Client, Sale, Invoice, ClientPrototipy, ClientUpdate

@app.post("/client", response_model=Client)
async def create_user(customerCreate: ClientPrototipy, session: SessionDep):
    customer = Client.model_validate(customerCreate.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.get("/client", response_model=list[Client])
async def get_clients(session: SessionDep):
    return session.exec(select(Client)).all()

@app.get("/client/{id}")
async def get_customer_Id(id: int, session: SessionDep):
    if not session.get(Client, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return session.get(Client, id)

@app.delete("/client/{id}")
async def delete_customer(id: int, session: SessionDep):
    customer = session.get(Client, id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    session.delete(customer)
    session.commit()
    return {"message": "Client deleted"}

@app.put("/client/{id}")
async def update_customer(id: int, customerUpdate: ClientPrototipy, session: SessionDep):
    customer = session.get(Client, id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    customer.name = customerUpdate.name
    customer.email = customerUpdate.email
    customer.age = customerUpdate.age
    customer.description = customerUpdate.description
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.patch("/client/{id}", status_code=status.HTTP_201_CREATED)
async def patch_customer(id: int, customerUpdate: ClientUpdate, session: SessionDep):
    customer = session.get(Client, id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    customer_data_updated = customerUpdate.model_dump(exclude_unset=True)
    customer.sqlmodel_update(customer_data_updated)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.post("/sale")
async def create_sale(sale: Sale):
    return sale

@app.post("/invoice")
async def create_invoice(invoice: Invoice):
    return invoice