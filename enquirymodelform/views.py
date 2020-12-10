from django.shortcuts import render
from .models import EnquiryModelData
from .forms import Enquirymodelform

# Create your views here.
def enquirymodelform(request):
    if request.method=='POST':
        form=Enquirymodelform(request.POST)
        if form.is_valid():
            form.save()

    form=Enquirymodelform()
    data=EnquiryModelData.objects.all()
    return render(request,'enquirymodelform/modelform.html',{'form':form,'data':data})