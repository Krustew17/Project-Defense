from rest_framework import serializers
from CarRental.car_app.models import CarModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'model']
