from django.urls import path
from enquirymodelform import views

urlpatterns = [
    path('modelform', views.enquirymodelform),
]