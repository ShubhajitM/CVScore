from fastapi import FastAPI
from uvicorn import run as uvicorn_run
from fastapi.middleware.cors import CORSMiddleware

from app.routers.cv_route import router as cv_route
from app.routers.job_route import router as job_route
from app.routers.lead_route import router as lead_route

app = FastAPI(title="CV Score API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(cv_route, prefix="/cv", tags=["CV analysis"])
app.include_router(job_route, prefix="/job", tags=["Job Details Management"])
app.include_router(lead_route, prefix="/leads", tags=["Lead Management"])


@app.get("/")
async def root():
    return {"message": "CV Score API is running"}


if __name__ == "__main__":
    uvicorn_run(app, host="0.0.0.0", port=8000)
