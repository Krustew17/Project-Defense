import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
import django.views.generic as views
from django.urls import reverse_lazy
from CarRental.car_app.models import CarListing
from CarRental.rent.forms import BaseRentForm
from CarRental.rent.models import RentModel, RentLogs
from CarRental.common.tasks import update_all_revenue_values


class RentCarView(LoginRequiredMixin, views.CreateView):
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
        # Car Listing
        car_listing = self.get_object()
        car_listing.is_available = False
        car_listing.save()

        # Rent Model
        rent_obj = form.save(commit=False)
        rent_obj.rented_to = self.request.user
        rent_obj.car_rented = car_listing
        rent_obj.save()

        rent_obj.rent_until = rent_obj.rent_date + datetime.timedelta(days=rent_obj.days)
        rent_obj.save()

        # Rent Logs
        revenue = car_listing.price * rent_obj.days
        RentLogs.objects.create(Car_Rented=car_listing,
                                days=rent_obj.days,
                                rented_to=self.request.user,
                                rented_from=car_listing.attached_user,
                                revenue=revenue)

        # Update Revenue
        update_all_revenue_values.delay(car_listing.attached_user.id)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user == self.car_listing.attached_user:
            messages.add_message(request, messages.ERROR, 'You cannot rent your own car!')
            return redirect('home page')


class RentSuccess(LoginRequiredMixin, views.TemplateView):
    template_name = 'rent/rent_success.html'
