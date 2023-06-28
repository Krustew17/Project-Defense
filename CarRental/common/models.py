import django.contrib.auth.base_user as auth_models
from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
# from CarRental.common.validators import validate_phone_number_length
from CarRental.core.utils import check_username_starts_with_letter
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class AppUser(auth_models.AbstractBaseUser):
    MIN_USERNAME_LENGTH = 6
    MAX_USERNAME_LENGTH = 18

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
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
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

    MAX_COUNTRY_LENGTH = 30
    MIN_COUNTRY_LENGTH = 3

    first_name = models.CharField(
        verbose_name='First Name',
        null=True,
        blank=True,
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
        )
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        null=True,
        blank=True,
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
        )
    )

    age = models.PositiveIntegerField(
        verbose_name='Age',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE),
        )
    )

    country = models.CharField(
        verbose_name='Country',
        null=True,
        blank=True,
        max_length=MAX_COUNTRY_LENGTH,
        validators=(
            MinLengthValidator(MIN_COUNTRY_LENGTH),
        )
    )
    phone_number = models.IntegerField(
        verbose_name="Phone Number",
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=AppUser)
def create_profile_user(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'profile'):
            ProfileUser.objects.create(user=instance)
