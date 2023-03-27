#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 01:59:41 2023

@author: alexandrubordanca
"""

from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    
    # Doctors views
   path('doctors/create/', views.doctors_create_view, name='doctors-create'),
   path('doctors/', views.doctors_list_view, name='doctors-list'),
   path('doctors/detail/', views.doctors_detail_view, name='doctors-detail'),
   path('doctors/choices/', views.doctors_view_choices, name='doctors-view-choices'),
   path('doctors/update/<int:id>/', views.doctors_update_view, name='doctors-update'),
   path('doctors/delete/<int:id>/', views.doctors_delete_view, name='doctors-delete'),

   # PatientContact views
   path('patient-contact/create/', views.pc_create_view, name='pc-create'),
   path('patient-contact/', views.pc_list_view, name='pc-list'),
   path('patient-contact/detail/', views.pc_detail_view, name='pc-detail'),
   path('patient-contact/choices/', views.pc_view_choices, name='pc-view-choices'),
   path('patient-contact/update/<int:id>/', views.pc_update_view, name='pc-update'),
   path('patient-contact/delete/<int:id>/', views.pc_delete_view, name='pc-delete'),

   # PatientDoctors views
   path('patient-doctors/create/', views.pd_create_view, name='pd-create'),
   path('patient-doctors/', views.pd_list_view, name='pd-list'),
   path('patient-doctors/detail/', views.pd_detail_view, name='pd-detail'),
   path('patient-doctors/choices/', views.pd_view_choices, name='pd-view-choices'),
   path('patient-doctors/update/<int:id>/', views.pd_update_view, name='pd-update'),
   path('patient-doctors/delete/<int:id>/', views.pd_delete_view, name='pd-delete'),

   # PatientFinance views
   path('patient-finance/create/', views.pf_create_view, name='pf-create'),
   path('patient-finance/', views.pf_list_view, name='pf-list'),
   path('patient-finance/detail/', views.pf_detail_view, name='pf-detail'),
   path('patient-finance/choices/', views.pf_view_choices, name='pf-view-choices'),
   path('patient-finance/update/<int:id>/', views.pf_update_view, name='pf-update'),
   path('patient-finance/delete/<int:id>/', views.pf_delete_view, name='pf-delete'),

   # PatientHealth views
   path('patient-health/create/', views.ph_create_view, name='ph-create'),
   path('patient-health/', views.ph_list_view, name='ph-list'),
   path('patient-health/detail/', views.ph_detail_view, name='ph-detail'),
   path('patient-health/choices/', views.ph_view_choices, name='ph-view-choices'),
   path('patient-health/update/<int:id>/', views.ph_update_view, name='ph-update'),
   path('patient-health/delete/<int:id>/', views.ph_delete_view, name='ph-delete'),
   
   # PatientVitals views
   path('patient-vitals/create/', views.pv_create_view, name='pv-create'),
   path('patient-vitals/', views.pv_list_view, name='pv-list'),
   path('patient-vitals/detail/', views.pv_detail_view, name='pv-detail'),
   path('patient-vitals/choices/', views.pv_view_choices, name='pv-view-choices'),
   path('patient-vitals/update/<int:id>/', views.pv_update_view, name='pv-update'),
   path('patient-vitals/delete/<int:id>/', views.pv_delete_view, name='pv-delete'),

   # PatientId views
   path('patient-id/create/', views.pid_create_view, name='pid-create'),
   path('patient-id/', views.pid_list_view, name='pid-list'),
   path('patient-id/detail/', views.pid_detail_view, name='pid-detail'),
   path('patient-id/choices/', views.pid_view_choices, name='pid-view-choices'),
   path('patient-id/update/<int:id>/', views.pid_update_view, name='pid-update'),
   path('patient-id/delete/<int:id>/', views.pid_delete_view, name = 'pid-delete')
]