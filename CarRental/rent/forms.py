from django import forms

from CarRental.rent.models import RentModel


class BaseRentForm(forms.ModelForm):
    class Meta:
        model = RentModel
        fields = ('location', 'days',)
