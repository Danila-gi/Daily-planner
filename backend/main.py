from fastapi import FastAPI
from api.routes import router
from db.database import db

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await db.init()

@app.on_event("shutdown")
async def startup_event():
    await db.close()