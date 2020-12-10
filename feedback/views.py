from django.shortcuts import render
from .models import FeedbackData
from .forms import Feedbackform

# Create your views here.
def feedback(request):
    form=Feedbackform()
    if request.method=='POST':
        form=Feedbackform(request.POST)
        if form.is_valid():
            name1=form.cleaned_data.get('name')
            email1 = form.cleaned_data.get('email')
            mobile1 = form.cleaned_data.get('mobile')

            data=FeedbackData(
                name=name1,
                email=email1,
                mobile=mobile1,
            )
            data.save()



    form=Feedbackform()
    feedback=FeedbackData.objects.all()
    return render(request,'feedback/feedback.html',{'form':form,'feedback':feedback})