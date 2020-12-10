from django.urls import path
from fakerapp import views

urlpatterns=[
    path('faker',views.insert),
]