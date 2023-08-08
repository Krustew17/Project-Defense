from django.urls import path, include
from .views import create_ad_view, CarListingDetails, DeleteCarView, Something, edit_car_listing

urlpatterns = (
    path('create-ad/', create_ad_view, name='create car ad'),
    path('something/', Something.as_view(), name='smth'),
    path('<int:pk>/', include([
        path('details/', CarListingDetails.as_view(), name='car ad details'),
        path('edit/', edit_car_listing, name='edit car ad'),
        path('delete/', DeleteCarView.as_view(), name='delete car ad')
    ]))
)
