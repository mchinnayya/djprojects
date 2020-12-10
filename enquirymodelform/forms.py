from django import forms
from .models import EnquiryModelData

class Enquirymodelform(forms.ModelForm):
    class Meta:
        model=EnquiryModelData
        fields='__all__'
