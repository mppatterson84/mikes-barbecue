from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "example@email.com", "class": "form-control"}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email Subject", "class": "form-control"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder": "Message", "class": "form-control"}))