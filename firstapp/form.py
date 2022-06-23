from django import forms
from .models import * 
class PersonForms(forms.ModelForm):
   

    
    class Meta:
        model = FirstModel
        fields = "__all__"