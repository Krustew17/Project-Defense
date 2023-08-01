from django.urls import path
from .views import RentCarView

urlpatterns = (
    path('<int:pk>/rent/', RentCarView.as_view(), name='Rent Car'),

)
