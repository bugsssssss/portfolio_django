from pyexpat import model
from django import forms

from homeapp.models import Feedback

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
        'name': 
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':"Your Name"
                }
            ),
        'email': 
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':"Your Email"

                }
            ),
        'text': 
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':"Your Message"

                }
            ),
        }