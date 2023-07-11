# Register your models here.
from CarRental.car_app.models import CarListing
from django.contrib import admin


@admin.register(CarListing)
class CarListingAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'price']
    list_filter = ['make', 'model', 'year', 'price', 'transmission', ]
    ordering = ['make', 'model', 'year', 'price']
    fieldsets = (
        ('Details', {'fields': ('make', 'model', 'year', 'price', 'transmission', 'engine_litres',
                                'mileage', 'horse_power', 'drive_type', 'engine_type', 'body_style', 'created',
                                'modified',
                                )}),
    )
    readonly_fields = ['created', 'modified']
    list_per_page = 20
