from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
import django.views.generic as views
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from datetime import date, timedelta
from django.utils import timezone
from CarRental.car_app.models import CarListing
from CarRental.rent.forms import BaseRentForm
from CarRental.rent.models import RentModel
from CarRental.common.tasks import update_all_revenue_values

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
        car_listing = self.get_object()
        car_listing.is_available = False
        car_listing.save()

        rent_obj = form.save(commit=False)
        rent_obj.rented_to = self.request.user
        rent_obj.rented_from = car_listing.attached_user
        rent_obj.car_rented = car_listing
        rent_obj.save()

        car_listing = self.get_object()
        car_listing.is_available = False
        car_listing.save()

        update_all_revenue_values.delay(car_listing.attached_user.id)

        return super().form_valid(form)


class RentSuccess(views.TemplateView):
    template_name = 'rent/rent_success.html'
