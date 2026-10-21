from fastapi import FastAPI
from storage.orm import init_db
from routes.url import router as url_router

app = FastAPI()

init_db()

app.include_router(url_router)