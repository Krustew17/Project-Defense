from django.urls import path, include
from .views import EditProfileDetailsView, profile_delete_view, ProfileDetailView

urlpatterns = (
    path('<int:pk>/', include([
        path('details/', ProfileDetailView.as_view(), name='profile details'),
        path('edit/', EditProfileDetailsView.as_view(), name='edit profile'),
        path('delete/', profile_delete_view, name='delete profile'),
    ])),
)
