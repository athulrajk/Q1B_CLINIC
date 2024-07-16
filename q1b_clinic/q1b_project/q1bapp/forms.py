#forms.py
from django import forms
from q1bapp.models import *
from .models import Eventappointment,Patient,Medicine


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        
class EventForm(forms.ModelForm):
    class Meta:
        model = Eventappointment
        fields = ['title', 'start_time', 'end_time', 'description','patient_id','treatment','notes','doctor']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['patient', 'drug_name', 'duration_date', 'instruction', 'note', 'dosage']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pateint_id', 'doctor', 'speciality', 'location', 'consultation_type', 'slot','date']
        widgets = {
            'pateint_id': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'consultation_type': forms.TextInput(attrs={'class': 'form-control'}),
            'slot': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
        self.fields['pateint_id'].error_messages = {'required': 'Patient ID is required.'}
        self.fields['doctor'].error_messages = {'required': 'Doctor is required.'}
        self.fields['speciality'].error_messages = {'required': 'Speciality is required.'}
        self.fields['location'].error_messages = {'required': 'Location is required.'}
        self.fields['consultation_type'].error_messages = {'required': 'Consultation type is required.'}
        self.fields['slot'].error_messages = {'required': 'Slot is required.'}