from django import forms
from app1.models import Table,Use
from app1.models import User
from django.contrib.auth.forms import UserCreationForm

class regfor(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Mail'}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class tbf(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Title'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Title Description'}))

    class Meta:
        model=Table
        fields=["title","description"]

class rf(forms.ModelForm):
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Commments'}))
    class Meta:
        model = Use
        fields = ['message']
