from django.db import models


class LanguageChoice(models.TextChoices):
    ENGLISH = 'en', 'English'
    SPANISH = 'es', 'Spanish'
    OTHER = 'other', 'Other'
