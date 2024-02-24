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
            'description',
            'attachment'
            ]
        labels = {
            'booking_date_time':'Booking date',
            'service':'Select a service or services',
            'description': 'Any additional Information',
            'attachment':'Any file or document you might want to attach',
            'budget':'Budget (Optional)'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, },),
            'booking_date_time': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
        }
