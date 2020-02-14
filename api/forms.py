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
        fields = ['firstname','lastname','visioneerEmailAddress','password','recoveryemail','recoveryphone','homeaddress','employeeid']

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = {'username', 'email','password1', 'password2','usn','dept','ut_id','phone_number' }

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()
