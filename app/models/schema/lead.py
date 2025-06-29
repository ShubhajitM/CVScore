from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class LeadStatus(str, Enum):
    NEW = "NEW"
    CONTACTED = "CONTACTED"
    QUALIFIED = "QUALIFIED"
    PROPOSAL_SENT = "PROPOSAL_SENT"
    NEGOTIATION = "NEGOTIATION"
    CLOSED_WON = "CLOSED_WON"
    CLOSED_LOST = "CLOSED_LOST"


class LeadCreate(BaseModel):
    first_name: Optional[str] = Field(None, description="First name of the lead")
    last_name: Optional[str] = Field(None, description="Last name of the lead")
    company: Optional[str] = Field(None, description="Company name")
    email_address: str = Field(..., description="Email address of the lead")
    project_description: Optional[str] = Field(None, description="Description of the project",)


class LeadResponse(BaseModel):
    lead_id: str = Field(..., description="Unique identifier for the lead")
    first_name: Optional[str] = Field(None, description="First name of the lead")
    last_name: Optional[str] = Field(None, description="Last name of the lead")
    company: Optional[str] = Field(None, description="Company name")
    email_address: str = Field(..., description="Email address of the lead")
    project_description: Optional[str] = Field(None, description="Description of the project")
    status: LeadStatus = Field(default=LeadStatus.NEW, description="Current status of the lead")
    created_at: datetime = Field(..., description="Timestamp when the lead was created")
    updated_at: datetime = Field(..., description="Timestamp when the lead was last updated") 