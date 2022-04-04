"""fit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('fit/', include('fit.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from cart.views import cart_add, cart_remove, cart_detail

from fit.views import register
from gym.authentication import user_login, logout_view
from gym.views import gym_list, gym_view, trainer_view, trainer_list, product_list, product_view, product_details_view, \
    order_list, history_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", product_list, name="home"),
    path('cart/', cart_detail, name='cart'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path(
        "product/<int:product_id>/", product_details_view, name="product_details_view"
    ),
    path('remove/<int:product_id>', cart_remove, name='cart_remove'),
    path("register/", register, name="register"),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path("gyms/", gym_list, name="gyms_list"),
    path("trainers/", trainer_list, name="trainer_list"),
    path('gym/<int:gym_id>', gym_view, name='gym_card'),
    path('trainer/<int:trainer_id>', trainer_view, name='trainer_view'),
    path("product/<int:product_id>", product_view, name="product_card"),
    path('order/', order_list, name='order'),
    path('history/', history_list, name='history')
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)