"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from home import views
from .views import handler400, handler403, handler404, handler429, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),        # Allauth
    path('summernote/', include('django_summernote.urls')),  # Summernote
    path('morphgun/', include('morphgun.urls')),       # Morphgun
    path('characters/', include('characters.urls')),  # Characters
    path('', include('home.urls')),                    # Home app URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = "main.views.handler400"
handler403 = "main.views.handler403"
handler404 = "main.views.handler404"
handler429 = "main.views.handler429"
handler500 = "main.views.handler500"
