from django import forms

from CarRental.rent.models import RentModel


class BaseRentForm(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(), label="Location", label_suffix="")
    days = forms.IntegerField(label='Days', label_suffix="")

    class Meta:
        model = RentModel
        fields = ('location', 'days',)
