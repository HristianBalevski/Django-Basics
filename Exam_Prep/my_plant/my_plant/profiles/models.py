from django.core.validators import MinLengthValidator
from django.db import models

from my_plant.profiles.validators import validate_starts_with_capital

USERNAME_MAX_LENGTH = 10
USERNAME_MIN_LENGTH = 2

FIRST_NAME_MAX_LENGTH = 20
LAST_NAME_MAX_LENGTH = 20


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=[MinLengthValidator(USERNAME_MIN_LENGTH),]
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[validate_starts_with_capital]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[validate_starts_with_capital]
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
