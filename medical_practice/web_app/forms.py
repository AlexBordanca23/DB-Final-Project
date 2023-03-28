#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:52:28 2023

@author: alexandrubordanca
"""

from django import forms
from .models import Doctors, PatientContact, PatientDoctors, PatientFinance, PatientHealth, PatientId, PatientVitals

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

class PatientFinanceForm(forms.ModelForm):
    class Meta:
        model = PatientFinance
        fields = '__all__'

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
