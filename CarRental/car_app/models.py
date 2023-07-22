from django.utils import timezone
from enum import Enum
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

User = get_user_model()


class CarMake(models.Model):
    MAX_MAKE_LENGTH = 16

    make = models.CharField(
        verbose_name='Make',
        max_length=MAX_MAKE_LENGTH,
        unique=True,
        choices=()
    )

    def __str__(self):
        return f"{self.make}"

    class Meta:
        ordering = ['make']
        verbose_name_plural = "Manufacturers"


# Create your models here.
class CarModel(models.Model):
    MAX_MODEL_LENGTH = 50
    MIN_MODEL_LENGTH = 1

    make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='models'
    )
    model = models.CharField(
        verbose_name='Car Model',
        max_length=MAX_MODEL_LENGTH,
        choices=(),
    )

    def __str__(self):
        return f"{self.model}"

    class Meta:
        ordering = ['make', 'model']
        unique_together = ('make', 'model')
        verbose_name_plural = 'Models'


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(c.name, c.value) for c in cls]

    @classmethod
    def max_length(cls):
        return max(len(c.value) for c in cls)


class CarListingBodyStyleChoices(ChoicesEnum):
    Sedan = 'Sedan'
    Coupe = 'Coupe'
    SUV = 'SUV'
    Hatchback = 'Hatchback'
    Sports = 'Sports Car'
    Wagon = 'Wagon'


class CarListingTransmissionChoices(ChoicesEnum):
    Manual = 'Manual'
    Automatic = 'Automatic'


class CarListingDriveTypeChoices(ChoicesEnum):
    FWD = 'FWD'
    RWD = 'RWD'
    AWD = 'AWD'


class CarListingEngineTypeChoices(ChoicesEnum):
    Petrol = 'Petrol'
    Diesel = 'Diesel'
    Hybrid = 'Hybrid'
    Electric = 'Electric'


class CarListingEuroChoices(ChoicesEnum):
    Euro_1 = 'Euro 1'
    Euro_2 = 'Euro 2'
    Euro_3 = 'Euro 3'
    Euro_4 = 'Euro 4'
    Euro_5 = 'Euro 5'
    Euro_6 = 'Euro 6'


class CarListing(models.Model):
    MAX_CAR_TITLE_LENGTH = 50
    MIN_CAR_TITLE_LENGTH = 5
    MIN_CAR_TITLE_LENGTH_MESSAGE = f"Your car title should be at least {MIN_CAR_TITLE_LENGTH} characters long."

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

    MIN_ENGINE_LITRES = 0.0
    MAX_ENGINE_LITRES = 8
    ENGINE_LITRES_MESSAGE = f"There's no bigger car engine than {MAX_ENGINE_LITRES} litres."

    car_title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CAR_TITLE_LENGTH,
        validators=(
            MinLengthValidator(MIN_CAR_TITLE_LENGTH, message=MIN_CAR_TITLE_LENGTH_MESSAGE),
        )
    )

    make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name="Manafacturer",
    )
    model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
        related_name='Car_Model',
    )

    year = models.IntegerField(
        verbose_name='Year',
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_YEAR),
        )
    )

    price = models.PositiveIntegerField(
        verbose_name='Price',
        null=False,
        blank=False,
    )

    transmission = models.CharField(
        verbose_name='Transmission',
        null=False,
        blank=False,
        max_length=CarListingTransmissionChoices.max_length(),
        choices=CarListingTransmissionChoices.choices()
    )

    engine_type = models.CharField(
        verbose_name='Engine Type',
        null=False,
        blank=False,
        max_length=CarListingEngineTypeChoices.max_length(),
        choices=CarListingEngineTypeChoices.choices()
    )
    engine_litres = models.FloatField(
        verbose_name='Engine Litres',
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_ENGINE_LITRES,
                              message=f'You cannot have an engine below {MIN_ENGINE_LITRES} litres.'),
            MaxValueValidator(MAX_ENGINE_LITRES, message=ENGINE_LITRES_MESSAGE),
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

    body_style = models.CharField(
        verbose_name='Body Style',
        null=False,
        blank=False,
        max_length=CarListingBodyStyleChoices.max_length(),
        choices=CarListingBodyStyleChoices.choices()
    )

    euro = models.CharField(
        verbose_name='Euro',
        null=False,
        blank=False,
        max_length=CarListingEuroChoices.max_length(),
        choices=(
            ('1', 'Euro 1'),
            ('2', 'Euro 2'),
            ('3', 'Euro 3'),
            ('4', 'Euro 4'),
            ('5', 'Euro 5'),
            ('6', 'Euro 6'),
        ),
    )

    drive_type = models.CharField(
        verbose_name='Drive Type',
        null=False,
        blank=False,
        max_length=CarListingDriveTypeChoices.max_length(),
        choices=CarListingDriveTypeChoices.choices()
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

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    @property
    def car_make_and_model(self):
        return f"{self.make} {self.model}"

    def delta(self):
        delta = timezone.now() - self.created
        seconds = int(delta.total_seconds())
        minutes = seconds // 60
        hours = minutes // 60
        days = hours // 24
        if days >= 1:
            return f"{days} days"
        elif minutes > 60:
            return f"{hours} hours"
        elif 1 <= minutes < 60:
            return f"{minutes} minutes"
        elif minutes < 1:
            return f"{seconds} seconds"


class PhotoCarModel(models.Model):
    MAX_IMAGES_ALLOWED = 3

    image = models.ImageField(upload_to='car_photos/', blank=True, null=True)
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={"quality": 60},
    )

    car = models.ForeignKey(
        to=CarListing,
        on_delete=models.CASCADE,
        related_name='car_pics'
    )

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    # def clean(self):
    #     if self.car.car_pics.all().count() > self.MAX_IMAGES_ALLOWED:
    #         raise ValidationError(f'You can upload up to {self.MAX_IMAGES_ALLOWED} images.')
