from fastapi import FastAPI
from app.api.drugs import router as drugs_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Drug copilot is runnung"
    }

app.include_router(
    drugs_router,
    prefix="/drugs"
)