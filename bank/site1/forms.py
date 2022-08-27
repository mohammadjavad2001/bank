from django import forms
class signupform(forms.Form):
   user = forms.CharField(label="Enter username",max_length = 100)
   password = forms.CharField(label="Enter password",widget = forms.PasswordInput())
   city = forms.CharField(label="Enter your city",max_length=50)


