from django import forms
from django.forms import ModelForm, Textarea, DateTimeField
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['user_name', 'product', 'rating', 'comment']
        widgets = {                    
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }