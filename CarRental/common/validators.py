from django.core.exceptions import ValidationError


def validate_phone_number_length(value):
    if len(value) != 10:
        raise ValidationError('Phone numbers consist of 10 digits.')
