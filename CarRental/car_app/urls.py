from django.urls import path, include
from .views import create_ad_view, view_car_ad_details, edit_car_ad, delete_car_ad, Something, test_html_css, \
    load_car_models

urlpatterns = (
    path('load_car_models/', load_car_models, name='load_car_models'),
    path('create-ad/', create_ad_view, name='create car ad'),
    path('something/', Something.as_view(), name='smth'),
    path('temp/', test_html_css, name='html_css test'),
    path('<int:pk>/', include([
        path('details/', view_car_ad_details, name='car ad details'),
        path('edit/', edit_car_ad, name='edit car ad'),
        path('delete/', delete_car_ad, name='delete car ad')
    ]))
)
