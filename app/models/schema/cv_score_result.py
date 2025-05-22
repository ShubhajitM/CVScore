from pydantic import BaseModel, Field, ValidationError


class CVScoreResult(BaseModel):
    score: int = Field(..., ge=0, le=100, description="Score between 0 and 100")
    feedback: str = Field(..., description="Brief feedback on the CV relevance")
