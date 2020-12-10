from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp_inherit/home.html')

def django(request):
    return render(request,'temp_inherit/django.html')

def mysql(request):
    return render(request,'temp_inherit/mysql.html')

def python(request):
    return render(request,'temp_inherit/python.html')