from django.core.exceptions import ValidationError


def check_if_name_is_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


def validate_passcode(value):
    if not (value.isdigit() and len(value) == 6):
        raise ValidationError("Your passcode must be exactly 6 digits!")
