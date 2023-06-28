from django.urls import path
from .views import HomePageView, CarListingsView, RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),
    path('catalogue/', CarListingsView.as_view(), name='car listings'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user')
)
