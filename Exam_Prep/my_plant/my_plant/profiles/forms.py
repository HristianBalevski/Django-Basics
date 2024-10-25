from django.forms import ModelForm
from my_plant.profiles.models import Profile


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class ProfileDetailsForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'profile_picture']


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'profile_picture']
