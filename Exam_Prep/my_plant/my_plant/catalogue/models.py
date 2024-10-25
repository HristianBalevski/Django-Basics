from django.core.validators import MinLengthValidator
from django.db import models

from my_plant.catalogue.validators import validate_only_letters

PLANT_TYPE_MAX_LENGTH = 14
PLANT_NAME_MAX_LENGTH = 20
PLANT_NAME_MIN_LENGTH = 2


class Plant(models.Model):
    INDOOR = 'indoor'
    OUTDOOR = 'outdoor'

    PLANT_CHOICES = [
        (INDOOR, 'Indoor Plants'),
        (OUTDOOR, 'Outdoor Plants'),
    ]

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_TYPE_MAX_LENGTH,
        choices=PLANT_CHOICES,
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(PLANT_NAME_MIN_LENGTH), validate_only_letters],
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False
    )


