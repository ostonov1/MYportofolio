from django import forms
from main.models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message()
        fields = '__all__'