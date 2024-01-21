from django.urls import path
from .views import RentCarView, RentSuccess

urlpatterns = (
    path('<int:pk>/rent/', RentCarView.as_view(), name='rent car'),
    path('rent/success/', RentSuccess.as_view(), name='rent success')

)
