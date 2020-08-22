from django import forms
from django.forms import ModelForm, Textarea
from .models import Class


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = '__all__'