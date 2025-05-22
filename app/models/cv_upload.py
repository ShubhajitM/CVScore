from pydantic import BaseModel, Field


class CvUpload(BaseModel):
    """Model for CV upload."""

    cv_file: str = Field(..., title="CV File", description="Base64 encoded CV file")
    user_id: str = Field(
        ..., title="User ID", description="ID of the user uploading the CV"
    )
    job_id: str = Field(
        ...,
        title="Job ID",
        description="ID of the job for which the CV is being uploaded",
    )
    timestamp: str = Field(
        ..., title="Timestamp", description="Timestamp of the upload"
    )
