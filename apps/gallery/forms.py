from django import forms
from apps.gallery.models import Characters, Videos, Synopsis

class CharactersForms(forms.ModelForm):
    class Meta:
        model = Characters
        exclude = ['published', ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'game': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class VideosForms(forms.ModelForm):
    class Meta:
        model = Videos
        exclude = ['posted', ]
        labels = {
            'narration': 'description'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'video': forms.FileInput(attrs={'class':'form-control'}),
            'thumb': forms.FileInput(attrs={'class':'form-control'}),
            'narration': forms.Textarea(attrs={'class':'form-control'})
        }

class SynopsisForms(forms.ModelForm):
    class Meta:
        model = Synopsis
        exclude = ['reveal', ]
        
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'games': forms.TextInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'})
        }