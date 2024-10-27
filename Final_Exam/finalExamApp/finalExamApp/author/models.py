from django.core.validators import MinLengthValidator
from django.db import models

from finalExamApp.author.validators import check_if_name_is_only_letters, validate_passcode

FIRST_NAME_MIN_LENGTH = 4
FIRST_NAME_MAX_LENGTH = 40

LAST_NAME_MIN_LENGTH = 2
LAST_NAME_MAX_LENGTH = 50


class Author(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(FIRST_NAME_MIN_LENGTH), check_if_name_is_only_letters]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(LAST_NAME_MIN_LENGTH), check_if_name_is_only_letters]
    )

    passcode = models.CharField(
        blank=False,
        null=False,
        validators=[validate_passcode],
        help_text="Your passcode must be a combination of 6 digits",
    )

    pets_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

