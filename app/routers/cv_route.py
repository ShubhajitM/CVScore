from typing import Annotated
from app.storage.job_db import JobDetailsEntity
from app.llm.cv_scoring import cv_scoring
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import uuid
import base64
from app.models.cv_upload import CvUpload
from app.models.schema.cv_score_result import CVScoreResult  # Import the missing class

router = APIRouter()


@router.post("/upload/{job_id}", response_model=CVScoreResult)
async def upload_cv(
    job_id: uuid.UUID,
    file: Annotated[UploadFile, File(description="upload cv file")],
):
    try:
        job_details = JobDetailsEntity.get_job_details(job_id)
        cv_file = await file.read()
        base64_encoded_data = base64.b64encode(cv_file)
        cv_file_base64 = base64_encoded_data.decode("utf-8")
        response = await cv_scoring.score_cv(job_details, cv_file_base64)
        return CVScoreResult(**response)
    except Exception as e:
        return {"error": str(e)}
