from django.core.exceptions import ValidationError


def validate_image_size(value):
    if value.size > 524880:
        raise ValidationError('The maximum allowed size is 5MB.')