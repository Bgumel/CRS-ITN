from django.db import models
from django.contrib.auth.models import User  # Import the User model


# Create your models here.

#distribution model
class ITNDistribution(models.Model):
    household_id = models.CharField(max_length=50, unique=True)
    household_head_name = models.CharField(max_length=100)
    number_of_family_members = models.PositiveIntegerField()
    itns_distributed = models.PositiveIntegerField()
    distribution_date = models.DateField()
    distributor_id = models.IntegerField( )  # Link to the User

    def __str__(self):
        return f"{self.household_id} - {self.household_head_name} distributed by {self.distributor.username}"
