# API schema
from pydantic import BaseModel, Field
from .models import ITNDistribution


# Schema for the User (distributor)
class UserSchema(BaseModel):
    id: int
    username: str

# Schema for ITNDistribution input, accepting just distributor_id
class ITNDistributionCreateSchema(BaseModel):
    household_id: str
    household_head_name: str
    number_of_family_members: int
    itns_distributed: int
    distribution_date: str
    distributor_id: int  # Expecting distributor_id in the input

class ITNDistributionSchema(BaseModel):
    household_id: str
    household_head_name: str
    number_of_family_members: int = Field(gt=0, description="Number of family members must be greater than zero")
    itns_distributed: int = Field(gt=0, description="ITNs distributed must be greater than zero")
    distribution_date: str
    distributor_id: UserSchema
