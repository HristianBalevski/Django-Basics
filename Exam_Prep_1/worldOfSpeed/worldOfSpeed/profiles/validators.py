from django.core.exceptions import ValidationError


def validate_username_min_length(value):
    if len(value) < 3:

        raise ValidationError("Username must be at least 3 chars long!")


def validate_username_allowed_symbols(value):
    for char in value:
        if not char.isalnum() and not char == '_':
            raise ValidationError("Username must contain only letters, digits, and underscores!")


def validate_minimum_age(value):
    if value < 21:
        raise ValidationError("")

