from django.contrib.auth import get_user_model
import django.contrib.auth.views as auth_views
from django.shortcuts import render
import django.views.generic as views
from django.urls import reverse_lazy

from CarRental.common.models import ProfileUser
from CarRental.profile_app.forms import ProfileBaseForm, EditProfileForm, EditPasswordForm

User = get_user_model()


# Create your views here.
class ProfileDetailView(views.DetailView):
    template_name = 'profile/profile_details.html'
    context_object_name = 'user'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileBaseForm
        context['pf'] = EditPasswordForm(user=self.request.user)
        return context


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


def profile_delete_view(request, pk):
    pass
