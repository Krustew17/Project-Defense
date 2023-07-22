import django_filters
from django.db import models
from django_filters import widgets as df
from django.forms import widgets

from .models import CarListing, CarMake


class CarFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    year = django_filters.RangeFilter()
    mileage = django_filters.RangeFilter()
    horse_power = django_filters.RangeFilter()
    engine_litres = django_filters.RangeFilter(widget=df.RangeWidget(attrs={'class': 'custom-field'}))

    class Meta:
        model = CarListing
        exclude = ('created', 'modified', 'attached_user')
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.ChoiceFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains'
                }
            }
        }
