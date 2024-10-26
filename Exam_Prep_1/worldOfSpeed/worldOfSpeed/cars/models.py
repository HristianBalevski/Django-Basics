from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeed.cars.validators import validate_year

TYPE_OF_CAR_MAX_LENGTH = 10

MODEL_MAX_LENGTH = 15
MODEL_MIN_LENGTH = 1

MINIMUM_PRICE = 1.0


class Car(models.Model):
    RALLY = 'Rally'
    OPEN_WHEEL = 'Open-Wheel'
    KART = 'Kart'
    DRAG = 'Drag'
    OTHER = 'Other'

    TYPE_CHOICES = [
        (RALLY, 'Rally'),
        (OPEN_WHEEL, 'Open-Wheel'),
        (KART, 'Kart'),
        (DRAG, 'Drag'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(
        blank=False,
        null=False,
        max_length=TYPE_OF_CAR_MAX_LENGTH,
        choices=TYPE_CHOICES,
        verbose_name="Type",
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MODEL_MAX_LENGTH,
        validators=[MinLengthValidator(MODEL_MIN_LENGTH)]
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[validate_year]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        unique=True,
        default="https://...",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one.",
        }
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(MINIMUM_PRICE)]
    )

    owner = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name='cars',
    )
