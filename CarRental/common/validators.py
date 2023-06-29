from functools import wraps
from typing import Any, Callable
from django.core.exceptions import ValidationError


# def validate_phone_number_length(phone_number_length: int) -> Callable:
#     @wraps(validate_phone_number_length)
#     def func1(value: int):
#         if len(str(value)) != phone_number_length:
#             raise ValidationError(f"Phone Number should consist of {phone_number_length + 1} digits.")
#
#     return func1


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
