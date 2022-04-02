"""fit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('fit/', include('fit.urls'))
"""
from django.contrib import admin
from django.urls import path

from fit.views import register
from gyms.views import index, gym_list, gym_view, trainer_view, trainer_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("register/", register, name="register"),
    path("gyms/", gym_list, name="gyms_list"),
    path("trainers/", trainer_list, name="trainer_list"),
    path('gym/<int:gym_id>', gym_view, name='gym_card'),
    path('coach/<int:coach_id>', trainer_view, name='trainer_view'),
    path("register/", register, name="register"),
]
