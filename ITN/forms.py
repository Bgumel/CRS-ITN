from django import forms
from .models import ITNDistribution

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
