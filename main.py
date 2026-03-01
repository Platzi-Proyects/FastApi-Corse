# Fist Steps

from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# Date Time Endpoints

from datetime import datetime, date, timedelta

@app.get("/")
async def root():
    return {
        "date": date.today(),
        "time": datetime.now().time(),
        "datetime": datetime.now(),
        "timedelta": timedelta(days=1)
    }