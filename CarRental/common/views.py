import django.contrib.auth.mixins as auth_mixins
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from .forms import RegisterUserForm, LoginUserForm
from django.shortcuts import render
from django.views import generic as views

User = get_user_model()


# Create your views here.
class HomePageView(views.TemplateView):
    model = User
    template_name = 'common/index.html'


class CarListingsView(views.TemplateView):
    template_name = 'car/car_listings.html'


class RegisterUserView(views.CreateView):
    template_name = 'common/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'common/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('home page')


class LogoutUserView(auth_views.LogoutView, auth_mixins.LoginRequiredMixin):
    template_name = 'common/logout.html'


class PageNotFoundView(views.TemplateView):
    template_name = 'common/404.html'
