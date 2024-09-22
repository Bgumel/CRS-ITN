# api.py
from ninja import Router
from django.shortcuts import get_object_or_404
from .models import ITNDistribution
from .schemas import ITNDistributionSchema
from ninja.errors import HttpError
from django.contrib.auth.models import User

router = Router()

# POST endpoint to submit ITN distribution data
    
@router.post("/distribution/", response={201: ITNDistributionSchema, 400: str})
def create_itn_distribution(request, payload: ITNDistributionSchema):
    try:
        
        # Create the ITN distribution record using the User object for distributor
        distribution = ITNDistribution.objects.create(
            household_id=payload.household_id,
            household_head_name=payload.household_head_name,
            number_of_family_members=payload.number_of_family_members,
            itns_distributed=payload.itns_distributed,
            distribution_date=payload.distribution_date,
            distributor_id=payload.distributor_id  # Save User object
        )
        
        # Return serialized data, including full User object
        return 201, distribution
        
    except Exception as e:
        return 400, f"Error creating ITN distribution: {str(e)}"


# GET endpoint to retrieve all ITN distributions
@router.get("/distributions/", response={200: list[ITNDistributionSchema], 400: str})
def get_itn_distributions(request):
    try:
        distributions = ITNDistribution.objects.all()
        return 200, distributions  # Directly return the queryset, ModelSchema will serialize it
    except Exception as e:
        return 400, f"Error retrieving ITN distributions: {str(e)}"


#GET endpoint to retrieve ITN distribution records by distributor_id
@router.get("/distributions/by_distributor/", response={200: list[ITNDistributionSchema], 404: str})
def get_distributions_by_distributor(request, distributor_id: int):
    try:
        # Fetch distributions for the given distributor_id
        distributions = ITNDistribution.objects.filter(distributor_id=distributor_id)
        
        if not distributions.exists():
            return 404, f"No distributions found for distributor_id: {distributor_id}"
        
        return 200, distributions
    except Exception as e:
        return 404, f"Error retrieving distributions: {str(e)}"