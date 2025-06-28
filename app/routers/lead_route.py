from typing import List
from fastapi import APIRouter, HTTPException
from app.models.schema.lead import LeadCreate, LeadResponse, LeadStatus
from app.storage.lead_db import lead_entity

router = APIRouter()


@router.post("/register", response_model=LeadResponse)
async def register_lead(lead_data: LeadCreate):
    """Register a new lead"""
    try:
        lead = lead_entity.create_lead(lead_data)
        return lead
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to register lead: {str(e)}")


@router.get("/{lead_id}", response_model=LeadResponse)
async def get_lead(lead_id: str):
    """Get a specific lead by ID"""
    try:
        lead = lead_entity.get_lead(lead_id)
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        return lead
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get lead: {str(e)}")


@router.put("/{lead_id}/status", response_model=LeadResponse)
async def update_lead_status(lead_id: str, status: LeadStatus):
    """Update lead status"""
    try:
        lead = lead_entity.update_lead_status(lead_id, status)
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        return lead
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update lead status: {str(e)}")


@router.get("/", response_model=List[LeadResponse])
async def get_all_leads():
    """Get all leads"""
    try:
        leads = lead_entity.get_all_leads()
        return leads
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get leads: {str(e)}") 