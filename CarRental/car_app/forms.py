from django import forms

from CarRental.car_app.models import CarModel, PhotoCarModel, CarListing, CarMake
from CarRental.core.utils import MultipleFileField


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = CarListing
        exclude = ('attached_user',)


class CreateCarForm(BaseCarForm):
    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), empty_label="-------")
    model = forms.ModelChoiceField(queryset=CarModel.objects.none(), empty_label="-------")

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

    class Meta:
        model = PhotoCarModel
        fields = ('image',)

    def clean_images(self):
        images = self.cleaned_data.get(['image'])
        print(images)
        if len(images) > 3:
            raise forms.ValidationError('test')
        return images
