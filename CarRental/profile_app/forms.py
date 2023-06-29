from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import FileInput

from CarRental.common.models import ProfileUser


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('profile_image', 'first_name', 'last_name', 'age', 'phone_number', 'country', 'city',)


class EditProfileForm(ProfileBaseForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control onerror'}), label="First Name",
                                 label_suffix="", required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control onerror'}), label="Last Name",
                                label_suffix="", required=False)
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control onerror'}), label="Age",
                             label_suffix="", required=False)

    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control onerror'}), label="Country",
                              label_suffix="", required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control onerror'}), label="City",
                           label_suffix="", required=False)
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control onerror'}),
                                      label="Profile Number", label_suffix="", required=False, initial=359)

    profile_image = forms.ImageField(widget=forms.FileInput(), label="Profile Image", label_suffix="", required=False)


class EditPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control onerror'}),
                                   label="Old Password", label_suffix="")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control onerror'}),
                                    label="New Password", label_suffix="")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control onerror'}),
                                    label="New Password Again", label_suffix="")
