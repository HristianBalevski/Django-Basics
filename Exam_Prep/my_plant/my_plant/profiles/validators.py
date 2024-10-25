from django.core.exceptions import ValidationError


def validate_starts_with_capital(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")