from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

from CarRental.common.models import ContactUsModel
from CarRental.common.validators import validate_phone_number_starts_with_zero

User = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    MAX_USERNAME_LENGTH = 16
    MIN_USERNAME_LENGTH = 3

    MAX_PASSWORD_LENGTH = 18
    MIN_PASSWORD_LENGTH = 8

    username = forms.CharField(
        required=True,
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
        ),
        widget=forms.TextInput(
            attrs={
                'class': 'user-box onerror',
                'autofocus': True,
            },
        ),
        label="Username",
        label_suffix=""
    )

    password1 = forms.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        required=True,
        validators=(
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'user-box',
            }
        ),
        label="Password",
        label_suffix=""
    )
    password2 = forms.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        required=True,
        validators=(
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'user-box',
            }
        ),
        label="Confirm Password",
        label_suffix=""
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(auth_forms.AuthenticationForm):
    MAX_USERNAME_LENGTH = 16
    MIN_USERNAME_LENGTH = 2

    MAX_PASSWORD_LENGTH = 18
    MIN_PASSWORD_LENGTH = 8

    username = forms.CharField(
        required=True,
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
        ),
        widget=forms.TextInput(
            attrs={
                'class': 'user-box onerror',
                'autofocus': True,
            },
        ),
        label="Username",
        label_suffix=""
    )

    password = forms.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        required=True,
        validators=(
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'user-box',
            }
        ),
        label="Password",
        label_suffix=""
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    topic = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))

    class Meta:
        model = ContactUsModel
        fields = "__all__"
