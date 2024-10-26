from django.forms import ModelForm
from django import forms

from worldOfSpeed.profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
