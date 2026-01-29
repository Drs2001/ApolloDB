from django import forms
from .models import Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['company_name', 'url', 'location', 'email', 'position', 'application_date']  # List the fields to include in the form

        # Optional: Customize field widgets (for better UI or control)
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'application_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
