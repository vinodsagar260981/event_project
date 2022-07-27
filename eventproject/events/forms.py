from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels ={
            'name': '',
            'address': '',
            'zip_code': '', 
            'phone': '', 
            'web': '', 
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Address'}),
            'zip_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Zip Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Web'}),
            'email_address' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue','manager', 'description', 'attendees')
        labels ={
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'description': '', 
            'attendees': 'Attendees',
        }
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Enter Venue'}), 
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'manager'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}), 
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Enter Attendees'}),
        }