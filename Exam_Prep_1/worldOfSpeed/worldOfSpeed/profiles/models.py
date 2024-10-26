from django.db import models

from worldOfSpeed.profiles.validators import validate_username_min_length, validate_username_allowed_symbols, \
    validate_minimum_age

USERNAME_MAX_LENGTH = 15

PASSWORD_MAX_LENGTH = 20

FIRST_NAME_MAX_LENGTH = 25

LAST_NAME_MAX_LENGTH = 25


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            validate_username_min_length,
            validate_username_allowed_symbols,
        ]
    )

    email = models.EmailField(blank=False, null=False)

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=[validate_minimum_age],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=PASSWORD_MAX_LENGTH,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=LAST_NAME_MAX_LENGTH,
    )

    profile_picture = models.URLField(blank=True, null=True)
