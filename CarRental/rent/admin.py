from django.contrib import admin
from django.utils.html import format_html
from CarRental.rent.models import RentModel, RentLogs


@admin.register(RentModel)
class RentAdmin(admin.ModelAdmin):
    list_display = ['rented_to', 'days', 'location', 'Rent_status', '_']
    ordering = ['rent_date', 'days', 'rent_status']
    list_filter = ['days', 'rent_status', 'rent_date']
    readonly_fields = ['rent_date', 'rent_until']
    list_per_page = 12
    fieldsets = (
        ('Details',
         {'fields': ('rent_status', 'rented_to', 'location', 'days', 'rent_date', 'rent_until')}),
    )

    def _(self, obj):
        if obj.rent_status == 'Rented':
            return True
        elif obj.rent_status == 'Pending':
            return None
        else:
            return False

    _.boolean = True

    def Rent_status(self, obj):
        if obj.rent_status == 'Rented':
            color = '#28a745'
        elif obj.rent_status == 'Pending':
            color = 'orange'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.rent_status))

    Rent_status.allow_tags = True


# @admin.register(RentLogs)
# class LogsAdmin(admin.ModelAdmin):
#     list_display = ['rented_from', 'rented_to', 'Car_Rented_id', 'days', 'revenue', 'rent_date']
#     ordering = ['revenue', 'days']
#     list_filter = ['rented_from', 'rented_to', 'Car_Rented_id', 'days', 'revenue', 'rent_date']
#     readonly_fields = ['rent_date', 'revenue']
#     list_per_page = 20
#     fieldsets = (
#         ('Details',
#          {'fields': ('rented_from', 'rented_to', 'revenue', 'days', 'rent_date', 'car_rented')}),
#     )
