from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
async def upload_cv():
    # Placeholder function to simulate CV upload
    return {"message": "CV uploaded successfully"}