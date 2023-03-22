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
    path('create/',views.doctors_create_view, name = 'create'),
    path('view/',views.doctors_list_view, name = 'list_view'),
    path('view/<int:id>',views.doctors_detail_view, name = "detail_view"),
    path('update/<int:id>/',views.doctors_update_view,name = 'update'),
    path('delete/<int:id>/', views.doctors_delete_view, name='delete'),
    path('view_choices/',views.doctors_view_choices, name ='view_choices'),
]