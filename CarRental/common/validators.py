from functools import wraps
from typing import Any, Callable
from django.core.exceptions import ValidationError

from CarRental import settings
from CarRental.core.utils import megabytes_to_bytes


def validate_image_size(obj):
    filesize = obj.file.size
    if filesize > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f"Max file size is {settings.MAX_MEGABYTES_UPLOAD}MB")


def validate_only_characters(field_name: str) -> Callable:
    @wraps(validate_only_characters)
    def func(value: Any):
        for char in value:
            if not char.isalpha():
                raise ValidationError(f"{field_name.title()} can contain only characters.")

    return func


def validate_phone_number_starts_with_zero(value):
    if len(str(value)) != 9 or str(value)[0] != "8":
        print(str(value)[1])
        raise ValidationError("Invalid phone number format. Try: 08xxxxxxxx")


def check_username_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your username should start with a letter.')
