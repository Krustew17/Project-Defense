import datetime
from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import formats

from CarRental import settings

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

    location = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LOCATION_LENGTH,
    )

    days = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    rented_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Rented_to_User',
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
        until = self.rent_date + datetime.timedelta(days=self.days)
        until = formats.date_format(until, settings.DATETIME_FORMAT)
        return until

    def __str__(self):
        return f"{self.location}"

    class Meta:
        verbose_name_plural = 'Rent Requests'
