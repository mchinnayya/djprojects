from django import forms
from multiselectfield import MultiSelectFormField


class EnquiryForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.IntegerField()

    course_choice = (
        ('django', 'django'),
        ('python', 'python'),
        ('mysql', 'mysql')
    )
    course=MultiSelectFormField(choices=course_choice,max_length=200)

    location_choice = (
        ('Hyderabad', 'Hyderabad'),
        ('Delhi', 'Delhi'),
        ('Bengalore', 'Bengalore')
    )
    location = MultiSelectFormField(choices=location_choice, max_length=200)

    gender_choice=(
        ('male','male'),('female','female')
    )
    gender = forms.MultipleChoiceField(choices=gender_choice,
                                       widget=forms.RadioSelect)

    date = forms.DateField(
        widget=forms.SelectDateWidget
    )

