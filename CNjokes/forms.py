
from django import forms
from .models import CNJoke

class CNJokeForm(forms.ModelForm):
    class Meta:
        model = CNJoke
        fields = ['joke']    