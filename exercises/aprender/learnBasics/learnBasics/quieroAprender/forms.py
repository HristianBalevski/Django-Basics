from django import forms

from learnBasics.quieroAprender.choices import LanguageChoice
from learnBasics.quieroAprender.models import Post


class PersonForm(forms.Form):
    PROGRAMMING_CHOICES = (
        (1, 'Python'),
        (2, 'JavaScript'),
        (3, 'Java'),
        (4, 'Ruby'),
        (5, 'PHP'),
    )
    person_name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter your age'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    # programming_language = forms.IntegerField(widget=forms.Select(choices=PROGRAMMING_CHOICES))
    programming_language = forms.ChoiceField(choices=PROGRAMMING_CHOICES)
    are_you_student = forms.BooleanField(required=False)
    comment = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # content = forms.CharField(widget=forms.Textarea)
    # date_posted = forms.DateField()
    # language = forms.CharField(choices=LanguageChoice.choices)
    # author = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = '__all__'


class DeletePost(PostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


