from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)