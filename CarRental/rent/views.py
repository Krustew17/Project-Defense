from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
import django.views.generic as views
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin

from CarRental.car_app.models import CarListing
from CarRental.rent.forms import BaseRentForm
from CarRental.rent.models import RentModel


# Create your views here.
class RentCarView(views.CreateView, LoginRequiredMixin):
    model = RentModel
    form_class = BaseRentForm
    template_name = 'rent/rent_car.html'
    success_url = reverse_lazy('rent success')

    def get_object(self, queryset=None):
        return get_object_or_404(CarListing, pk=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        self.car_listing = self.get_object()  # not using self.object to avoid clashes
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_listing'] = self.get_object()
        return context

    def form_valid(self, form):
        rent_obj = form.save(commit=False)
        rent_obj.rented_to = self.request.user
        rent_obj.save()
        return super().form_valid(form)


class RentSuccess(views.TemplateView):
    template_name = 'rent/rent_success.html'