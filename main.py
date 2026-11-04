from fastapi import FastAPI

from routes.url import router as url_router

app = FastAPI()

app.include_router(url_router)