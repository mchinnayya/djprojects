
from django.urls import path
from temp_inhet import views

urlpatterns=[
    path('',views.home),
    path('django',views.django,name="django"),
    path('mysql',views.mysql),
    path('python',views.python),
]