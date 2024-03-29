"""
URL configuration for CarRental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse, reverse_lazy
from django.views.generic import RedirectView

from CarRental.common.views import PageNotFoundView

urlpatterns = [
    # Admin
    # path('admin1/', RedirectView.as_view(url=reverse_lazy('admin:home page'))),
    path('admin/', admin.site.urls),

    # Common
    path('', include('CarRental.common.urls')),

    # Car
    path('car/', include('CarRental.car_app.urls')),

    # User Profile
    path('profile/', include('CarRental.profile_app.urls')),

    # REST API
    path('api/', include('CarRental.api.urls')),

    # Rent
    path('car/', include('CarRental.rent.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = PageNotFoundView.as_view()
