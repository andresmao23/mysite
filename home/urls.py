"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home import views
from home.views import SitioList

urlpatterns = [
    url(r'^$', views.index, name='inicio'),
    url(r'^nosotros/', views.nosotros, name='nosotros'),
    url(r'^sitios', SitioList.as_view(), name='sitios'),
    url(r'^contactenos/', views.contactenos, name='contactenos'),
    url(r'^gracias/', views.gracias, name='gracias'),
    url(r'^sitio/detalle/(?P<id_sitio>\d+)$', views.detalle_sitio, name='detalle'),
]
