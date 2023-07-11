import django_filters
from .models import CarModel, CarListing


class CarFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    year = django_filters.RangeFilter()

    class Meta:
        model = CarListing
        fields = {
            'make': ['exact'],
            'model': ['exact'],
            # 'body_style': ['exact'],
            # 'horse_power': ['lte', 'gte'],
            # 'mileage': ['lt', 'gt'],
            # 'transmission': ['exact']
        }
