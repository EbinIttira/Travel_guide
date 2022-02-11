from django import forms
from .models import myplaces

class updateform(forms.ModelForm):
    class Meta:
        model=myplaces
        fields=['place','desc','district','img']