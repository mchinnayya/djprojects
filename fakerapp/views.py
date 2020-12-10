from django.shortcuts import render
from django.http import HttpResponse
from .models import FakerData
import faker
fake = faker.Faker()

# Create your views here.
def insert(request):

    for i in range(10):
        fname=fake.fname()
        lname=fake.lname()
        email=fake.email()
        job=fake.job()
        salary=fake.salary()
        city=fake.city()
        dob=fake.date_time()
        address=fake.salary()

        fakedata = FakerData(
            fname=fname,
            lname=lname,
            email=email,
            job=job,
            salary=salary,
            city=city,
            dob=dob,
            address=address
        )
        fakedata.save()
    return HttpResponse("data saved")