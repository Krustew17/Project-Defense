from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

User = get_user_model()


# Create your models here.
class CarModel(models.Model):
    MAX_MAKE_LENGTH = 16
    MIN_MAKE_LENGTH = 3

    MAX_MODEL_LENGTH = 16
    MIN_MODEL_LENGTH = 1

    MIN_PRICE = 1

    MIN_BODY_STYLE_LENGTH = 4
    MAX_BODY_STYLE_LENGTH = 10

    MIN_YEAR = 1886

    MIN_HORSE_POWER = 1

    MIN_MILEAGE = 1

    MIN_COLOR_LENGTH = 2
    MAX_COLOR_LENGTH = 16

    MIN_TRANSMISSION_LENGTH = 4
    MAX_TRANSMISSION_LENGTH = 16

    MIN_DRIVE_TYPE_LENGTH = 1
    MAX_DRIVE_TYPE_LENGTH = 8

    MIN_FUEL_TYPE_LENGTH = 2
    MAX_FUEL_TYPE_LENGTH = 12

    MAX_EURO_LENGTH = 10

    MAX_ENGINE_TYPE_LENGTH = 10

    make = models.CharField(
        verbose_name='Make',
        null=False,
        blank=False,
        max_length=MAX_MAKE_LENGTH,
        validators=(
            MinLengthValidator(MIN_MAKE_LENGTH),
        )
    )
    model = models.CharField(
        verbose_name='Car Model',
        null=False,
        blank=False,
        max_length=MAX_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_MODEL_LENGTH),
        )
    )

    price = models.IntegerField(
        verbose_name='Price',
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

    body_style = models.CharField(
        verbose_name='Body Style',
        null=False,
        blank=False,
        max_length=MAX_BODY_STYLE_LENGTH,
        validators=(
            MinLengthValidator(MIN_BODY_STYLE_LENGTH),
        )
    )

    year = models.IntegerField(
        verbose_name='Year',
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_YEAR),
        )
    )

    horse_power = models.IntegerField(
        verbose_name='Horse Power',
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_HORSE_POWER),
        )
    )

    mileage = models.IntegerField(
        verbose_name='Mileage',
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_MILEAGE),
        )
    )
    euro = models.CharField(
        verbose_name='Euro',
        null=False,
        blank=False,
        max_length=MAX_EURO_LENGTH
    )

    transmission = models.CharField(
        verbose_name='Transmission',
        null=False,
        blank=False,
        max_length=MAX_TRANSMISSION_LENGTH,
        validators=(
            MinLengthValidator(MIN_TRANSMISSION_LENGTH),
        )
    )

    drive_type = models.CharField(
        verbose_name='Drive Type',
        null=False,
        blank=False,
        max_length=MAX_DRIVE_TYPE_LENGTH,
        validators=(
            MaxLengthValidator(MAX_DRIVE_TYPE_LENGTH),
        )
    )

    engine_type = models.CharField(
        verbose_name='Engine Type',
        null=False,
        blank=False,
        max_length=MAX_ENGINE_TYPE_LENGTH,
        validators=(
            MinLengthValidator(MIN_FUEL_TYPE_LENGTH),
        )
    )

    color = models.CharField(
        verbose_name='Color',
        null=False,
        blank=True,
        max_length=MAX_COLOR_LENGTH,
        validators=(
            MinLengthValidator(MIN_COLOR_LENGTH),
        )
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    attached_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='cars_attached',
    )


class PhotoCarModel(models.Model):
    MAX_IMAGES_ALLOWED = 3

    image = models.ImageField(upload_to='car_photos/', blank=True, null=True, )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={"quality": 60},
    )

    car = models.ForeignKey(
        to=CarModel,
        on_delete=models.CASCADE,

    )

    def clean(self):
        if len(self.image) > self.MAX_IMAGES_ALLOWED:
            raise ValidationError(f'You can upload up to {self.MAX_IMAGES_ALLOWED} images.')
