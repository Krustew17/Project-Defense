from enum import Enum
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from CarRental.car_app.models import CarListing

User = get_user_model()


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(c.name, c.value) for c in cls]

    @classmethod
    def max_length(cls):
        return max(len(c.value) for c in cls)


class StatusChoices(ChoicesEnum):
    Pending = 'Pending'
    Rented = 'Rented'
    Cancelled = 'Cancelled'

class RentModel(models.Model):
    MAX_LOCATION_LENGTH = 60

    MIN_RENT_DAYS = 1
    MIN_RENT_DAYS_ERROR_MESSAGE = f'You need to rent a car for at least {MIN_RENT_DAYS} days.'

    location = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LOCATION_LENGTH,
    )

    days = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_RENT_DAYS, message=MIN_RENT_DAYS_ERROR_MESSAGE),
        )
    )

    car_rented = models.ForeignKey(
        CarListing,
        on_delete=models.CASCADE,
        related_name='car_rented_rent_model'
    )

    rented_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='car_rented_to_user',
    )

    rent_status = models.CharField(
        null=False,
        blank=False,
        max_length=StatusChoices.max_length(),
        choices=StatusChoices.choices(),
        default='Pending'
    )
    rent_date = models.DateTimeField(
        auto_now_add=True,
    )
    rent_until = models.DateTimeField(
        default=None,
        null=True,
    )

    def __str__(self):
        return f"{self.location}"

    class Meta:
        verbose_name_plural = 'Rent Requests'


class RentLogs(models.Model):
    MAX_DECIMAL_FIELD_DIGITS = 10
    DECIMAL_FIELD_DECIMALS = 2

    car_rented = models.ForeignKey(
        CarListing,
        on_delete=models.SET_NULL,
        name='Car_Rented',
        null=True,
    )
    days = models.IntegerField(
        default=0,
    )
    rented_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='Rented_to_User',
        null=True,
    )

    rented_from = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Rented_from_User'
    )
    rent_date = models.DateTimeField(
        auto_now_add=True,
    )
    revenue = models.DecimalField(
        max_digits=MAX_DECIMAL_FIELD_DIGITS,
        decimal_places=DECIMAL_FIELD_DECIMALS,
        null=True,
    )

    def __str__(self):
        return f"{self.car_rented.car_title}, revenue: ${self.revenue}"

    class Meta:
        verbose_name_plural = 'Rent Logs'
