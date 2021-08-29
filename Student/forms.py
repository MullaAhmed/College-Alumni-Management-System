from django import forms

class sendmessage(forms.Form):
    name=forms.CharField(label="Name",max_length=1000)
    body=forms.CharField(label="body",required=False)