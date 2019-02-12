"""blogengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    # path('', home, name='home'),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('blog/', include('blog.urls')),
]

urlpatterns += [
    url(r'^catalog/', include('catalog.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns += [
#     path('logout/', include('django.contrib.auth.urls')),
# ]
