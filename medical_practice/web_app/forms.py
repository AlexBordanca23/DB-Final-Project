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
        fields = ['first_name', 'last_name']

class PatientContactForm(forms.ModelForm):
    class Meta:
        model = PatientContact
        fields = ['email', 'street_address', 'city', 'state', 'zip']

class PatientDoctorsForm(forms.ModelForm):
    class Meta:
        model = PatientDoctors
        fields = ['doctor']

class PatientFinanceForm(forms.ModelForm):
    class Meta:
        model = PatientFinance
        fields = ['amount_due', 'ins_co']

class PatientHealthForm(forms.ModelForm):
    class Meta:
        model = PatientHealth
        fields = ['current_smoker', 'condition_1', 'condition_2', 'condition_3', 'condition_4', 'condition_5', 'condition_6', 'condition_7', 'condition_8', 'condition_9', 'condition_10']

class PatientIdForm(forms.ModelForm):
    class Meta:
        model = PatientId
        fields = ['firstname', 'lastname', 'dob', 'age', 'biol_sex', 'ethnicity']

class PatientVitalsForm(forms.ModelForm):
    class Meta:
        model = PatientVitals
        fields = ['last_height', 'last_weight']
