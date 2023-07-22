from django.urls import path

from CarRental.api.views import load_car_models

urlpatterns = (
    path('load_car_models/', load_car_models, name='load_car_models'),
)
