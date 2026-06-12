from django import forms
from apps.employee.models import Identify

class IdentifyForms(forms.ModelForm):
    class Meta:
        model = Identify
        exclude = ['post', ]

        widgets = {
            'identify': forms.TextInput(attrs={'class':'form-control'})
        }