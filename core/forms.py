from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            'service', 
            'full_name', 
            'phone_number',
            'email_address',
            'booking_date_time',
            'location',
            'expected_number_of_guests',
            'budget',
            'description'
            ]
        widgets = {
            'service': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        label = {
            'booking_date_time':'booking date'
        }
