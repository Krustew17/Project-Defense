import datetime
from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import formats, timezone

from CarRental import settings
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


# Create your models here.
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
        on_delete=models.CASCADE
    )

    rented_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Rented_to_User',
    )

    rented_from = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Rented_from_User'
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

    @property
    def rent_until(self):
        # until = self.rent_date + datetime.timedelta(days=self.days)
        until = self.rent_date + datetime.timedelta(minutes=1, hours=3)
        until = formats.date_format(until, settings.DATETIME_FORMAT)
        return until

    @property
    def calculate_revenue(self):
        return self.days * self.car_rented.price

    def __str__(self):
        return f"{self.location}"

    class Meta:
        verbose_name_plural = 'Rent Requests'
