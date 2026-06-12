from django import forms
from apps.about.models import AboutUs

class AboutUsForms(forms.ModelForm):
    class Meta:
        model = AboutUs
        exclude = ['published', ]

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'profile' : forms.FileInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'}),
            'role' : forms.TextInput(attrs={'class':'form-control'})
        }