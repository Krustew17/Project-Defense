import django.contrib.auth.views as auth_views
from django.urls import path, include
from .views import HomePageView, CarListingsView, register_user_view, LoginUserView, LogoutUserView, ContactUsView, \
    FriendlyAskedQuestions, activate_user_view, PasswordReset, PasswordResetDone, \
    PasswordResetComplete, PasswordResetConfirm

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),
    path('catalogue/', CarListingsView.as_view(), name='car listings'),

    path('register/', register_user_view, name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),

    path('password/reset/', include([
        path('', PasswordReset.as_view(), name='password_reset'),
        path('reset-password-email-sent/', PasswordResetDone.as_view(), name='password_reset_done'),
        path('<uidb64>/<token>/',
             PasswordResetConfirm.as_view(), name='password_reset_confirm'),
        path('done/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    ])),

    path('activate-user/<uidb64>/<token>', activate_user_view, name='activate'),

    path('contact-us/', ContactUsView.as_view(), name='contact us'),
    path('faq/', FriendlyAskedQuestions.as_view(), name='faq'),

)
