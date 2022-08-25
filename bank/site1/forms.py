from django import forms
class signup(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   city = forms.CharField(max_length=50)
   