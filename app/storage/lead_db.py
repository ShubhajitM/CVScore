import boto3
from datetime import datetime
import uuid
import os
from typing import Optional, List
from dotenv import load_dotenv
from app.models.schema.lead import LeadStatus, LeadCreate, LeadResponse

# Load environment variables from .env file
load_dotenv()


class LeadEntity:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        # Make table name configurable via environment variable
        self.table_name = os.getenv('LEADS_TABLE_NAME', 'leads')
        print(f"Using table name: {self.table_name}")
        self.table = self.dynamodb.Table(self.table_name)

    def create_lead(self, lead_data: LeadCreate) -> LeadResponse:
        """Create a new lead in DynamoDB"""
        lead_id = str(uuid.uuid4())
        current_time = datetime.utcnow().isoformat()
        
        item = {
            'PK': 'LEADS',
            'SK': current_time,  # Using date as sort key
            'lead_id': lead_id,
            'first_name': lead_data.first_name,
            'last_name': lead_data.last_name,
            'company': lead_data.company,
            'email_address': lead_data.email_address,
            'project_description': lead_data.project_description,
            'status': LeadStatus.NEW.value,
            'created_at': current_time,
            'updated_at': current_time
        }
        
        self.table.put_item(Item=item)
        
        return LeadResponse(
            lead_id=lead_id,
            first_name=lead_data.first_name,
            last_name=lead_data.last_name,
            company=lead_data.company,
            email_address=lead_data.email_address,
            project_description=lead_data.project_description,
            status=LeadStatus.NEW,
            created_at=datetime.fromisoformat(current_time),
            updated_at=datetime.fromisoformat(current_time)
        )

    def get_lead(self, lead_id: str) -> Optional[LeadResponse]:
        """Get a lead by ID"""
        try:
            response = self.table.scan(
                FilterExpression='lead_id = :lead_id',
                ExpressionAttributeValues={':lead_id': lead_id}
            )
            
            if response['Items']:
                item = response['Items'][0]
                return LeadResponse(
                    lead_id=item['lead_id'],
                    first_name=item['first_name'],
                    last_name=item['last_name'],
                    company=item['company'],
                    email_address=item['email_address'],
                    project_description=item['project_description'],
                    status=LeadStatus(item['status']),
                    created_at=datetime.fromisoformat(item['created_at']),
                    updated_at=datetime.fromisoformat(item['updated_at'])
                )
            return None
        except Exception as e:
            print(f"Error getting lead: {e}")
            return None

    def update_lead_status(self, lead_id: str, status: LeadStatus) -> Optional[LeadResponse]:
        """Update lead status"""
        try:
            current_time = datetime.utcnow().isoformat()
            
            response = self.table.scan(
                FilterExpression='lead_id = :lead_id',
                ExpressionAttributeValues={':lead_id': lead_id}
            )
            
            if response['Items']:
                item = response['Items'][0]
                
                self.table.update_item(
                    Key={
                        'PK': item['PK'],
                        'SK': item['SK']
                    },
                    UpdateExpression='SET #status = :status, updated_at = :updated_at',
                    ExpressionAttributeNames={
                        '#status': 'status'
                    },
                    ExpressionAttributeValues={
                        ':status': status.value,
                        ':updated_at': current_time
                    }
                )
                
                return self.get_lead(lead_id)
            return None
        except Exception as e:
            print(f"Error updating lead status: {e}")
            return None

    def get_all_leads(self) -> List[LeadResponse]:
        """Get all leads"""
        try:
            response = self.table.scan()
            leads = []
            
            for item in response['Items']:
                leads.append(LeadResponse(
                    lead_id=item['lead_id'],
                    first_name=item['first_name'],
                    last_name=item['last_name'],
                    company=item['company'],
                    email_address=item['email_address'],
                    project_description=item['project_description'],
                    status=LeadStatus(item['status']),
                    created_at=datetime.fromisoformat(item['created_at']),
                    updated_at=datetime.fromisoformat(item['updated_at'])
                ))
            
            return leads
        except Exception as e:
            print(f"Error getting all leads: {e}")
            return []


# Global instance
lead_entity = LeadEntity() 