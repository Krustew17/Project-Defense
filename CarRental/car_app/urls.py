from django.urls import path, include
from .views import create_ad_view, view_car_ad_details, edit_car_ad, delete_car_ad, TestImage, Something

urlpatterns = (
    path('create-ad/', create_ad_view, name='create car ad'),
    path('test/', TestImage.as_view(), name='test'),
    path('something/', Something.as_view(), name='smth'),
    path('<int:pk>/', include([
        path('details/', view_car_ad_details, name='car ad details'),
        path('edit/', edit_car_ad, name='edit car ad'),
        path('delete/', delete_car_ad, name='delete car ad')
    ]))
)
