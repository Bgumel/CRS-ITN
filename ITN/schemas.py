# API schema
from .models import ITNDistribution
from ninja import Schema
from pydantic import Field, validator
from datetime import date

class ITNDistributionSchema(Schema):
    household_id: str = Field(..., min_length=1, max_length=100)
    household_head_name: str
    number_of_family_members: int
    itns_distributed: int
    distribution_date: date
    distributor_id: int

    @validator('number_of_family_members', 'itns_distributed')
    def must_be_positive(cls, value):
        if value < 1:
            raise ValueError('This field must be a positive number.')
        return value
