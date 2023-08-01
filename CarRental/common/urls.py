from django.urls import path, include
from .views import HomePageView, CarListingsView, register_user_view, LoginUserView, LogoutUserView, ContactUsView, \
    FriendlyAskedQuestions, activate_user_view

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),
    path('catalogue/', CarListingsView.as_view(), name='car listings'),
    path('register/', register_user_view, name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('contact-us/', ContactUsView.as_view(), name='contact us'),
    path('faq/', FriendlyAskedQuestions.as_view(), name='faq'),
    path('activate-user/<uidb64>/<token>', activate_user_view, name='activate')
)
