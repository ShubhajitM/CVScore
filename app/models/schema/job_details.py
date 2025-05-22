from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class JobDetails(BaseModel):
    job_id: str = Field(..., max_length=36, description="Unique identifier for the job")
    job_title: str = Field(..., max_length=100, description="Title of the job")
    job_type: str = Field(
        ...,
        max_length=50,
        description="Type of job (e.g., Full-time, Part-time, Contract)",
    )
    company_name: Optional[str] = None
    location: Optional[str] = None
    job_description: str = Field(
        ..., description="Description of the job responsibilities and requirements"
    )
    salary_range: Optional[str] = None
