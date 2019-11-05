from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User,Visioneer
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model = User
        fields = '__all__'


class ResetCustomForm(forms.ModelForm):
    class Meta:
        fields  = '__all__'


class VisioneerForm(forms.ModelForm):
    class Meta:
        model=Visioneer
        fields = '__all__'