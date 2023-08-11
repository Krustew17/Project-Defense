from django.urls import path, include
from .views import create_ad_view, CarListingDetails, DeleteCarView, edit_car_listing

urlpatterns = (
    path('create-ad/', create_ad_view, name='create car ad'),
    path('<int:pk>/', include([
        path('details/', CarListingDetails.as_view(), name='car ad details'),
        path('edit/', edit_car_listing, name='edit car ad'),
        path('delete/', DeleteCarView.as_view(), name='delete car ad')
    ]))
)
