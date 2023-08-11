import django_filters
from django_filters import widgets as df

from .models import CarListing


class CarFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(label="$/Day")
    year = django_filters.RangeFilter()
    mileage = django_filters.RangeFilter()
    horse_power = django_filters.RangeFilter()
    engine_litres = django_filters.RangeFilter(widget=df.RangeWidget(attrs={'class': 'custom-field'}))

    class Meta:
        model = CarListing
        exclude = ('created', 'modified', 'attached_user', 'is_available')
