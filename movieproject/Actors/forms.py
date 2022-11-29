from django import forms

from .models import Actor

class actform(forms.ModelForm):
    class Meta:
        model=Actor
        fields=['name','des']
