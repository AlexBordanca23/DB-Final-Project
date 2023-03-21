#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 01:59:41 2023

@author: alexandrubordanca
"""

from django.urls import path

from . import views 

urlpatterns = [
path('', views.home, name = 'home')
]