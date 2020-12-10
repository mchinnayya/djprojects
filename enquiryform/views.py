from django.shortcuts import render
from .models import EnquiryData
from .forms import EnquiryForm

# Create your views here.
def enquiryform(request):
    form=EnquiryForm()
    if request.method=='POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data.get('name')
            email1 = form.cleaned_data.get('email')
            mobile1 = form.cleaned_data.get('mobile')
            course1 = form.cleaned_data.get('course')
            location1 = form.cleaned_data.get('location')
            gender1 = form.cleaned_data.get('gender')
            date1 = form.cleaned_data.get('date')

            data=EnquiryData(
                name=name1,
                email=email1,
                mobile=mobile1,
                course=course1,
                location=location1,
                gender=gender1,
                date=date1,
            )
            data.save()

    form=EnquiryForm()
    enquiry=EnquiryData.objects.all()
    return render(request,'enquiryform/enquiryform.html',{'form':form,'enquiry':enquiry})