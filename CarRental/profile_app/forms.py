from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from CarRental.common.models import ProfileUser


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('first_name', 'last_name', 'age', 'country', 'phone_number', 'profile_image')


class EditProfileForm(ProfileBaseForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-box onerror'}), label="First Name",
                                 label_suffix="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-box onerror'}), label="Last Name",
                                label_suffix="")
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'user-box onerror'}), label="Age",
                             label_suffix="")

    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-box onerror'}), label="Country",
                              label_suffix="")


class EditPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control oneerror'}),
                                   label="Old Password", label_suffix="")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control oneerror'}),
                                    label="New Password", label_suffix="")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control oneerror'}),
                                    label="New Password Again", label_suffix="")