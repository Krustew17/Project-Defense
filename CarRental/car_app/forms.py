from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError

from CarRental.car_app.models import CarModel, PhotoCarModel, CarListing, CarMake
from CarRental.core.utils import MultipleFileField


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = CarListing
        exclude = ('attached_user',)


class CreateCarForm(BaseCarForm):
    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), empty_label="-------")
    model = forms.ModelChoiceField(queryset=CarModel.objects.none(), empty_label="-------")
    price = forms.IntegerField(label="$/Day: ", label_suffix="")

    def __init__(self, *args, **kwargs):
        super(CreateCarForm, self).__init__(*args, **kwargs)
        self.fields['make'].widget.attrs['onchange'] = 'load_car_models(this.value);'

    def get_models_by_make(self, make_id):
        return CarModel.objects.filter(make_id=make_id).values('id', 'model')

    def clean_make(self):
        make = self.cleaned_data['make']
        self.fields['model'].queryset = CarModel.objects.filter(make=make)
        return make


class EditCarForm(BaseCarForm):
    pass


# ~~~~~ Car Photo below ~~~~~

class AttachPhotosToCar(forms.ModelForm):
    image = MultipleFileField()
    image.label = "Images:"

    class Meta:
        model = PhotoCarModel
        fields = ('image',)
    #
    # def clean_image(self):
    #     images = self.cleaned_data.get('image', [])
    #     return images
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     images = cleaned_data.get('image', [])
    #     if len(images) > 3:
    #         print('error')
    #         raise ValidationError('You can only upload up to 3 images.')
