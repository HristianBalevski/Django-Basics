from django.forms import ModelForm
from django import forms

from finalExamApp.author.models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

        widgets = {

            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',

            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',

            }),
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',

            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',

            }),
        }


class EditAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
