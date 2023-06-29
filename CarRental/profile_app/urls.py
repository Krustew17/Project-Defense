from django.urls import path, include
from .views import EditProfileDetailsView, DeleteProfileView, ProfileDetailView, EditPasswordView

urlpatterns = (
    path('<int:pk>/', include([
        path('details/', ProfileDetailView.as_view(), name='profile details'),
        path('edit/', EditProfileDetailsView.as_view(), name='edit profile'),
        path('password/change/', EditPasswordView.as_view(), name='edit password'),
        path('delete/', DeleteProfileView.as_view(), name='delete profile'),
    ])),
)
