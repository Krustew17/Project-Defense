from enum import Enum
import django.contrib.auth.base_user as auth_models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from CarRental.common.validators import validate_phone_number_starts_with_zero
from django.dispatch import receiver
from django.db.models.signals import post_save
from CarRental.common.validators import check_username_starts_with_letter
from CarRental.common.validators import validate_image_size


# Create your models here.
class AppUser(auth_models.AbstractBaseUser, PermissionsMixin):
    MIN_USERNAME_LENGTH = 6
    MAX_USERNAME_LENGTH = 18

    MAX_EMAIL_LENGTH = 60

    MAX_EMAIL_TOKEN_LENGTH = 200

    username = models.CharField(
        verbose_name='Username',
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            check_username_starts_with_letter,
        ),
        error_messages={
            'unique': "A user with that username already exists.",
        }
    )
    email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_EMAIL_LENGTH,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()


class ProfileUser(models.Model):
    MAX_FIRST_NAME_LENGTH = 20
    MIN_FIRST_NAME_LENGTH = 3

    MAX_LAST_NAME_LENGTH = 20
    MIN_LAST_NAME_LENGTH = 3

    MIN_AGE = 18
    MAX_AGE = 70
    AGE_VALIDATION_MESSAGE = f"You have to be between {MIN_AGE} and {MAX_AGE} to rent a car."

    MAX_COUNTRY_LENGTH = 30
    MIN_COUNTRY_LENGTH = 3

    MAX_CITY_LENGTH = 30

    PHONE_NUMBER_LENGTH = 9

    DEFAULT_REVENUE_TODAY = 0
    DEFAULT_REVENUE_YESTERDAY = 0
    DEFAULT_REVENUE_LAST_WEEK = 0
    DEFAULT_REVENUE_LAST_MONTH = 0
    DEFAULT_TOTAL_REVENUE = 0

    MAX_REVENUE_DIGITS = 10
    REVENUE_DECIMALS = 2

    profile_image = models.ImageField(
        verbose_name='Profile Image',
        null=True,
        blank=True,
        upload_to='profile_pictures/',
        validators=(
            validate_image_size,
        )
    )

    first_name = models.CharField(
        verbose_name='First Name',
        null=True,
        blank=True,
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            RegexValidator(regex="^[A-Za-z]+$", inverse_match=False,
                           message="First Name field can contain only characters."),
            # validate_only_characters(field_name='first name')
        )
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        null=True,
        blank=True,
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            RegexValidator(regex="^[A-Za-z]+$", inverse_match=False,
                           message="Last Name field can contain only characters."),
            # validate_only_characters(field_name='last name')
        )
    )

    age = models.PositiveIntegerField(
        verbose_name='Age',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE, message=AGE_VALIDATION_MESSAGE),
            MaxValueValidator(MAX_AGE, message=AGE_VALIDATION_MESSAGE),
        ),
        default=18,
    )

    country = models.CharField(
        verbose_name='Country',
        null=True,
        blank=True,
        max_length=MAX_COUNTRY_LENGTH,
        validators=(
            MinLengthValidator(MIN_COUNTRY_LENGTH),
            RegexValidator(regex="^[A-Za-z]+$", inverse_match=False,
                           message="Country field can contain only characters."),
            # validate_only_characters(field_name='country'),
        )
    )
    phone_number = models.IntegerField(
        verbose_name="Phone Number",
        null=True,
        blank=True,
        unique=True,
        validators=(
            validate_phone_number_starts_with_zero,
        )
    )

    city = models.CharField(
        verbose_name='City',
        max_length=MAX_CITY_LENGTH,
        null=True,
        blank=True,
        validators=(
            RegexValidator(regex="^[A-Za-z]+$", inverse_match=False, message="City field can contain only characters."),
            # validate_only_characters(field_name='city'),
        ),
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else ""

    @property
    def image_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User Profile"


class UserRevenue(models.Model):
    MAX_REVENUE_DIGITS = 10
    REVENUE_DECIMALS = 0

    DEFAULT_REVENUE_TODAY = 0
    DEFAULT_REVENUE_YESTERDAY = 0
    DEFAULT_REVENUE_LAST_WEEK = 0
    DEFAULT_REVENUE_LAST_MONTH = 0
    DEFAULT_TOTAL_REVENUE = 0

    revenue_today = models.DecimalField(
        max_digits=MAX_REVENUE_DIGITS,
        decimal_places=REVENUE_DECIMALS,
        default=DEFAULT_REVENUE_TODAY
    )
    revenue_yesterday = models.DecimalField(
        max_digits=MAX_REVENUE_DIGITS,
        decimal_places=REVENUE_DECIMALS,
        default=DEFAULT_REVENUE_YESTERDAY
    )
    revenue_last_week = models.DecimalField(
        max_digits=MAX_REVENUE_DIGITS,
        decimal_places=REVENUE_DECIMALS,
        default=DEFAULT_REVENUE_LAST_WEEK
    )
    revenue_last_month = models.DecimalField(
        max_digits=MAX_REVENUE_DIGITS,
        decimal_places=REVENUE_DECIMALS,
        default=DEFAULT_REVENUE_LAST_MONTH
    )
    total_revenue = models.DecimalField(
        max_digits=MAX_REVENUE_DIGITS,
        decimal_places=REVENUE_DECIMALS,
        default=DEFAULT_TOTAL_REVENUE
    )
    revenue_last_updated = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='revenue'
    )


@receiver(post_save, sender=AppUser)
def create_profile_user(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'profile'):
            ProfileUser.objects.create(user=instance)


@receiver(post_save, sender=AppUser)
def create_revenue_user(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'revenue'):
            UserRevenue.objects.create(user=instance)


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(c.name, c.value) for c in cls]

    @classmethod
    def max_length(cls):
        return max(len(c.value) for c in cls)


class AdminMessage(ChoicesEnum):
    Read = 'Read'
    Unread = 'Unread'


class StatusMessage(ChoicesEnum):
    Pending = 'Pending'
    Solved = 'Solved'
    Unsolved = 'Unsolved'


class ContactUsModel(models.Model):
    MAX_NAME_LENGTH = 30

    MAX_TOPIC_LENGTH = 35

    MAX_MESSAGE_LENGTH = 300
    name = models.CharField(
        verbose_name='Name',
        null=False,
        blank=False,
        max_length=MAX_NAME_LENGTH,
        validators=(
            RegexValidator(regex="[a-zA-Z]+", inverse_match=False, message="Name field can contain only characters."),
        )
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    admin_message = models.CharField(
        null=True,
        max_length=AdminMessage.max_length(),
        choices=AdminMessage.choices(),
        default='Unread',
    )
    status = models.CharField(
        null=True,
        max_length=StatusMessage.max_length(),
        choices=StatusMessage.choices(),
        default='Pending',
    )
    email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
    )
    topic = models.CharField(
        verbose_name='Topic',
        null=False,
        blank=False,
        max_length=MAX_TOPIC_LENGTH,
    )

    message = models.TextField(
        verbose_name='Message',
        null=False,
        blank=False,
        max_length=MAX_MESSAGE_LENGTH,
    )

    def __str__(self):
        return f"Name: {self.name}, Topic: {self.topic}"

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us Requests"
