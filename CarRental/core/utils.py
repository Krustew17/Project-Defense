from django.core.exceptions import ValidationError


def check_username_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your username should start with a letter.')


def validate_username_only_letters_and_numbers(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Your username should consist of letters and numbers.')
