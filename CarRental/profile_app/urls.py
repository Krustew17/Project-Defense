from django.urls import path, include
from .views import profile_edit_view, profile_delete_view, profile_detail_view

urlpatterns = (
    path('<int:pk>/', include([
        path('details/', profile_detail_view, name='profile details'),
        path('edit', profile_edit_view, name='edit profile'),
        path('delete/', profile_delete_view, name='delete profile'),
    ])),
)
