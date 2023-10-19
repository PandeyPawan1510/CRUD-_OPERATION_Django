from django import forms
from. models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields="__all__"

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields="__all__"



