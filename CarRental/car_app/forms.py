from django import forms

from CarRental.car_app.models import CarModel, PhotoCarModel
from CarRental.core.utils import MultipleFileField


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ('attached_user',)


class CreateCarForm(BaseCarForm):
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
