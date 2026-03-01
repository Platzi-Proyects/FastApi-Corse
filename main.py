# Fist Steps

from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# Date Time Endpoints

from datetime import datetime
from zoneinfo import ZoneInfo

currentTimezone = {
    "EST": "America/New_York",
    "PST": "America/Los_Angeles",
    "GMT": "Europe/London",
    "UTC": "UTC",
    "IST": "Asia/Kolkata"
}

@app.get("/{iso_str}")
async def root(iso_str: str):
    iso = iso_str.upper()
    timesome_str = currentTimezone.get(iso)
    tz = ZoneInfo(timesome_str)
    return {
        "time": datetime.now(tz).isoformat(),
    }
