import django.contrib.auth.mixins as auth_mixins
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from .forms import RegisterUserForm, LoginUserForm, ContactUsForm
from django.shortcuts import render, redirect
from django.views import generic as views

from ..car_app.models import CarListing

User = get_user_model()


# Create your views here.
class HomePageView(views.TemplateView):
    model = User
    template_name = 'common/index.html'


class CarListingsView(views.ListView):
    template_name = 'car/car_listings.html'
    model = CarListing
    paginate_by = 3

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)


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


class ContactUsView(views.FormView):
    form_class = ContactUsForm
    template_name = 'common/contact_us.html'

    def get_success_url(self):
        return reverse_lazy('home page')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['topic']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, email, ['krasitaskapp@gmail.com'])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        form.save(commit=True)
        return redirect('home page')


class FriendlyAskedQuestions(views.TemplateView):
    template_name = 'common/faq.html'
