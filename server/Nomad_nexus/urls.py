"""
URL configuration for Nomad_nexus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name = "home"),
    path("flights/", views.flights, name = "flights"),
    path("trains/", views.trains, name = "trains"),
    path("buses/", views.buses, name = "buses"),
    path("itenary/", views.itenary, name = "itenary"),
    path("add_itenary/", views.add_itenary, name = "add_itenary"),
    path("login/", views.login, name = "login"),
    path("payment_gateway", views.payment_gateway, name = "payment_gateway"),
    path("payment", views.payment, name = "payment"),
    path('logout/', views.logout_view, name='logout'),
]
