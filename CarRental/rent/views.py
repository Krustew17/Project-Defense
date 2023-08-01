from django.shortcuts import render
import django.views.generic as views


# Create your views here.
class RentCarView(views.TemplateView):
    template_name = 'rent/rent_car.html'
