from fastapi import FastAPI
from uvicorn import run as uvicorn_run

from app.routers.cv_route import router as cv_route

app = FastAPI(title="CV Score API", version="1.0.0")

app.include_router(cv_route, prefix="/cv", tags=["CV Management"])

@app.get("/")
async def root():
    return {"message": "CV Score API is running"}

if __name__ == "__main__":
    uvicorn_run(app, host="0.0.0.0", port=8000)

