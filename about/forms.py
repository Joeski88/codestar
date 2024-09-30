from .models import CollaborateRequest
from django import forms


class CollaborateForm(form.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')