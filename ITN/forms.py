from django import forms
from .models import ITNDistribution
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ITNDistributionForm(forms.ModelForm):
    class Meta:
        model = ITNDistribution
        fields = [
            'household_id', 
            'household_head_name', 
            'number_of_family_members', 
            'itns_distributed', 
            'distribution_date'
        ]
        widgets = {
            'household_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Household ID', 'min': 1}),
            'household_head_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Household Head Name'}),
            'number_of_family_members': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'itns_distributed': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'distribution_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_itns_distributed(self):
        itns = self.cleaned_data.get('itns_distributed')
        if itns < 1:
            raise forms.ValidationError("At least 1 ITN must be distributed.")
        return itns
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Override the help text for the username field
        self.fields['username'].help_text = "<br>Letters, digits and @/./+/-/_ only."  # Remove the help text completely

