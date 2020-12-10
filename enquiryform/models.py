from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class EnquiryData(models.Model):
    name=models.CharField(max_length=100)

    email=models.EmailField(max_length=100)

    mobile=models.BigIntegerField()

    course_choice=(
        ('django','django'),
        ('python','python'),
        ('mysql','mysql')
    )
    course=MultiSelectField(choices=course_choice,max_length=200)

    location_choice=(
        ('Hyderabad','Hyderabad'),
        ('Delhi','Delhi'),
        ('Bengalore','Bengalore')
    )
    location=MultiSelectField(choices=location_choice,max_length=200)

    gender=models.CharField(max_length=100)

    date=models.DateField(max_length=100)

    def __str__(self):
        return self.name

