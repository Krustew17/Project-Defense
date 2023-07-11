from django.urls import path, include
from .views import HomePageView, CarListingsView, RegisterUserView, LoginUserView, LogoutUserView, ContactUsView, \
    FriendlyAskedQuestions

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),  # Done
    path('catalogue/', CarListingsView.as_view(), name='car listings'),
    path('register/', RegisterUserView.as_view(), name='register user'),  # Done
    path('login/', LoginUserView.as_view(), name='login user'),  # Done
    path('logout/', LogoutUserView.as_view(), name='logout user'),  # Done
    path('contact-us/', ContactUsView.as_view(), name='contact us'),  # Done
    path('faq/', FriendlyAskedQuestions.as_view(), name='faq'),  # Done
)
