# Fist Steps

from pydantic import BaseModel, EmailStr
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

from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

@app.post("/user")
async def create_user(user: User):
    return user
    