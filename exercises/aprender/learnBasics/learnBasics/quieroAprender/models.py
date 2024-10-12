from django.db import models

from learnBasics.quieroAprender.choices import LanguageChoice


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    languages = models.CharField(max_length=20, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH)
    author = models.CharField(max_length=100, default='Anonymous')

    def __str__(self):
        return self.title

