from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ["from_email", "subject", "message"]
        widgets = {
            'from_email': forms.TextInput(attrs={"placeholder": "example@email.com", "class": "form-control"}),
            'subject': forms.TextInput(attrs={"placeholder": "Email Subject", "class": "form-control"}),
            'message': forms.Textarea(attrs={"placeholder": "Message: 700 characters max.", "class": "form-control"}),
        }