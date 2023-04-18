"""
URL configuration for projectmentoring project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from mentoring.urls import urlpatterns as mentoring_urls

urlpatterns = [
    # mentoring app url patterns
    path('mentoring/', include(mentoring_urls))
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('api-auth/', include('rest_framework.urls')))
    # drf spectacular
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
    urlpatterns.append(path('api/schema/', SpectacularAPIView.as_view(), name='schema'))
    urlpatterns.append(path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'))
    urlpatterns.append(path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'))
    # Redirect api root to Swagger UI
    from django.views.generic import RedirectView
    urlpatterns.append(path('', RedirectView.as_view(url='api/schema/swagger-ui/', permanent=False), name='api-root'))
