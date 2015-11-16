from django import forms


class LoginForm(forms.Form):
    account = forms.CharField(widget=forms)
    passwd = forms.CharField(widget=forms.PasswordInput)
