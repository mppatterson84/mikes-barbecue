from django.contrib import admin
from django.urls import path

from .views import emailView, SuccessPageView

urlpatterns = [
    path('contact/', emailView, name='contact'),
    path('success/', SuccessPageView.as_view(), name='success'),
]