from typing import Annotated
from app.storage.job_db import JobDetailsEntity, job_details_map
from app.llm.cv_scoring import cv_scoring
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import uuid
import base64
from app.models.cv_upload import CvUpload
from app.models.schema.cv_score_result import CVScoreResult  # Import the missing class
from app.models.schema.job_details import JobDetails  # Import the missing class

router = APIRouter()


@router.post("/create", response_model=dict)
async def upload_cv(job_details: JobDetails):
    try:
        JobDetailsEntity.add_job_details(
            job_id=job_details.job_id,
            job_title=job_details.job_title,
            job_description=job_details.job_description,
            job_type=job_details.job_type,
        )
        return {
            "job_id": str(job_details.job_id),
            "message": "Job details added successfully",
        }
    except Exception as e:
        return {"error": str(e)}


@router.get("/get/{job_id}", response_model=str)
async def get_job_details(job_id: uuid.UUID):
    try:
        print(f"Fetching job details for job_id: {job_id}")
        return job_details_map.get(str(job_id), None)
    except Exception as e:
        return {"error": str(e)}
