"""foodtasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from foodtaskerapp import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('restaurant/sign-in',include("django.contrib.auth.urls"),
    #{'template_name':'restaurant/sign_i.html'}, name='restaurant-sign-in'),
    #path('restaurant/sign-out', LogoutView,
    #{'next_page':'/'}, name='restaurant-sign-out'),
    path('restaurant/',include("django.contrib.auth.urls")),
    path('restaurant/sign-up', views.restaurant_sign_up, name='restaurant-sign-up'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
