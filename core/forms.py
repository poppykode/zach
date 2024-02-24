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
            'description': forms.Textarea(attrs={'rows': 4,'class': 'form-control form-control-lg form-control-a'},),
            'booking_date_time': forms.DateInput(attrs={'class': 'form-control form-control-lg form-control-a datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            'service':  forms.SelectMultiple(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}), 
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'email_address':  forms.EmailInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'location':  forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'expected_number_of_guests':  forms.NumberInput(attrs={'class': 'form-control form-control-lg form-control-a datepicker'}),
            'budget':  forms.NumberInput(attrs={'class': 'form-control form-control-lg form-control-a','step':'0.01'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
        }

class ContactForm(forms.Form):
    full_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control form-control-lg form-control-a','placeholder':'Enter full name'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control form-control-lg form-control-a','placeholder':'Enter email'}))
    subject = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control form-control-lg form-control-a','placeholder':'Enter subject'}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':4,'class':'form-control form-control-lg form-control-a','placeholder':'Enter message'}))
