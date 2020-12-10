from django.shortcuts import render,redirect
from .models import Task
from .forms import Taskform

# Create your views here.
def create(request):
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()

    form=Taskform()
    task=Task.objects.all()
    return render(request,'task/create.html',{'form':form,'task':task})

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/create')

def update(request,id):
    task=Task.objects.get(id=id)
    form=Taskform(instance=task)
    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/create')

    context={'form':form,'task':task}
    return render(request,'task/update.html',context)




