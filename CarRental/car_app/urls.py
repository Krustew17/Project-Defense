from django.urls import path, include
from .views import create_car_ad, view_car_ad_details, edit_car_ad, delete_car_ad

urlpatterns = (
    path('create-ad/', create_car_ad, name='create car ad'),
    path('<int:pk>/', include([
        path('details/', view_car_ad_details, name='car ad details'),
        path('edit/', edit_car_ad, name='edit car ad'),
        path('delete/', delete_car_ad, name='delete car ad')
    ]))
)
