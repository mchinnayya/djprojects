from django.urls import path
from task import views

urlpatterns = [
    path('create', views.create),
    path('delete/<str:id>/',views.delete),
    path('update/<str:id>/',views.update),


]