import django.contrib.auth.mixins as auth_mixins
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .forms import RegisterUserForm, LoginUserForm, ContactUsForm, ResetPasswordForm, SetNewPasswordForm
from django.shortcuts import render, redirect
from django.views import generic as views
from ..car_app.filters import CarFilter
from ..car_app.models import CarListing
from ..core.utils import generate_token, send_activation_email

User = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'common/index.html'


class CarListingsView(views.ListView):
    template_name = 'car/car_listings.html'
    model = CarFilter
    paginate_by = 6
    context_object_name = 'listings'
    queryset = CarListing.objects.filter(is_available=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CarFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_listings'] = CarListing.objects.all()
        context['form'] = self.filterset.form
        return context


def register_user_view(request):
    if request.method == 'GET':
        form = RegisterUserForm()
    else:
        form = RegisterUserForm(request.POST)

        username = request.POST.get('username')
        if form.is_valid():
            form.save()
            user = User.objects.get(username=username)
            send_activation_email(user, request)
            messages.add_message(request, messages.SUCCESS, "We sent you an email to verify your account.")
            return redirect('login user')

    context = {
        'form': form,
    }

    return render(request, 'common/register.html', context)


def activate_user_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.add_message(request, messages.SUCCESS, 'You have successfully verified your email.')
        return redirect(reverse('login user'))

    context = {
        'user': user
    }

    return render(request, 'authentication/activate-failed.html', context)


class LoginUserView(auth_views.LoginView):
    template_name = 'common/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('home page')


class LogoutUserView(auth_views.LogoutView, auth_mixins.LoginRequiredMixin):
    template_name = 'common/logout.html'


# ~~~~~~~~~~~ Password Reset ~~~~~~~~~~~~
class PasswordReset(auth_views.PasswordResetView):
    template_name = 'password_reset/password_reset.html'
    form_class = ResetPasswordForm


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'password_reset/password_reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset/password_reset_confirm.html'
    form_class = SetNewPasswordForm


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset/password_reset_complete.html'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PageNotFoundView(views.TemplateView):
    template_name = 'common/404.html'


class ContactUsView(auth_mixins.LoginRequiredMixin, views.FormView):
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
        messages.add_message(self.request, messages.SUCCESS, 'Thanks for contacting us!')
        return redirect('home page')


class FriendlyAskedQuestions(views.TemplateView):
    template_name = 'common/faq.html'
