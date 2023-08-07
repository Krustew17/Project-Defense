from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
import django.views.generic as views


# Create your views here.
class RentCarView(views.TemplateView, LoginRequiredMixin):
    template_name = 'rent/rent_car.html'
