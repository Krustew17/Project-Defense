from django.contrib.auth import get_user_model
import django.contrib.auth.views as auth_views
import django.contrib.auth.mixins as mixins
import django.views.generic as views
from django.urls import reverse_lazy

from CarRental.car_app.filters import CarFilter
from CarRental.car_app.models import CarListing, PhotoCarModel
from CarRental.common.models import ProfileUser
from CarRental.profile_app.forms import EditProfileForm, EditPasswordForm

User = get_user_model()


class ProfileDetailView(mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile_details.html'
    context_object_name = 'user'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_car_listings'] = CarListing.objects.filter(attached_user=self.request.user.id)
        return context


class UserListingsView(views.ListView):
    template_name = 'profile/user_car_listings.html'
    model = CarFilter
    paginate_by = 6
    context_object_name = 'listings'
    queryset = CarListing.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = CarListing.objects.filter(attached_user=self.request.user.id)
        self.filterset = CarFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_listings'] = CarListing.objects.filter(attached_user=self.request.user.id)
        context['form'] = self.filterset.form
        return context


class EditProfileDetailsView(mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/edit_profile.html'
    model = ProfileUser
    form_class = EditProfileForm
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class EditPasswordView(mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'profile/password_change.html'
    form_class = EditPasswordForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class DeleteProfileView(mixins.LoginRequiredMixin, views.DeleteView):
    model = User
    template_name = 'profile/delete_profile.html'

    def get_success_url(self):
        return reverse_lazy('home page')

    def form_valid(self, form):
        PhotoCarModel.objects.all().delete()
        CarListing.objects.all().delete()

        return super().form_valid(form)
