from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(required=True, label='username', max_length=200)
    password = forms.CharField(required=True, label='password', max_length=200)
    