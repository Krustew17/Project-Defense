from django import forms
from django.core.exceptions import ValidationError


def check_username_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your username should start with a letter.')


def validate_username_only_letters_and_numbers(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Your username should consist of letters and numbers.')


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
