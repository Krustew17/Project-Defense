from django.contrib.auth import get_user_model
import django.contrib.auth.views as auth_views
from django.shortcuts import render
import django.views.generic as views
from django.urls import reverse_lazy

from CarRental.car_app.models import CarListing, PhotoCarModel
from CarRental.common.forms import ContactUsForm
from CarRental.common.models import ProfileUser
from CarRental.profile_app.forms import ProfileBaseForm, EditProfileForm, EditPasswordForm

User = get_user_model()


# Create your views here.
class ProfileDetailView(views.DetailView):
    template_name = 'profile/profile_details.html'
    context_object_name = 'user'
    model = User


class EditProfileDetailsView(views.UpdateView):
    template_name = 'profile/edit_profile.html'
    model = ProfileUser
    form_class = EditProfileForm
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class EditPasswordView(auth_views.PasswordChangeView):
    template_name = 'profile/password_change.html'
    form_class = EditPasswordForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class DeleteProfileView(views.DeleteView):
    model = User
    template_name = 'profile/delete_profile.html'

    def get_success_url(self):
        return reverse_lazy('home page')

    def form_valid(self, form):
        PhotoCarModel.objects.all().delete()
        CarListing.objects.all().delete()

        return super().form_valid(form)
