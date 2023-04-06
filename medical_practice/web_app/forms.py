#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:52:28 2023

@author: alexandrubordanca
"""

from django import forms
from .models import Doctors, PatientContact, PatientDoctors, PatientFinance, PatientHealth, PatientId, PatientVitals
from django.urls import reverse_lazy
from dal import autocomplete

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'

class PatientContactForm(forms.ModelForm):
    class Meta:
        model = PatientContact
        fields = '__all__'

class PatientDoctorsForm(forms.ModelForm):
    class Meta:
        model = PatientDoctors
        fields = '__all__'

class PatientIdWidget(forms.TextInput):
    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['data-minimum-input-length'] = 2
        attrs['data-placeholder'] = 'Search for a patient ID'
        attrs['autocomplete'] = 'off'
        return attrs

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/i18n/en.min.js',
        )

    def __init__(self, attrs=None):
        super().__init__(attrs=attrs)

        self.attrs['class'] = 'django-select2 select2'

        self.choices = []
        for patient in PatientId.objects.all():
            self.choices.append((str(patient.patient_id), str(patient)))

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)

        if value:
            try:
                return PatientId.objects.get(patient_id=int(value))
            except (ValueError, PatientId.DoesNotExist):
                return None

        return None

    def get_url(self):
        return reverse_lazy('patient-autocomplete')
    
class PatientFinanceForm(forms.ModelForm):
    class Meta:
        model = PatientFinance
        fields = ['patient', 'amount_due', 'ins_co']
        widgets = {'patient': PatientIdWidget()}
        

        
class PatientHealthForm(forms.ModelForm):
    class Meta:
        model = PatientHealth
        fields = '__all__'

class PatientIdForm(forms.ModelForm):
    class Meta:
        model = PatientId
        fields = '__all__'

class PatientVitalsForm(forms.ModelForm):
    class Meta:
        model = PatientVitals
        fields = '__all__'
