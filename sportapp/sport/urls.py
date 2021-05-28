"""sport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('description/methodics/', views.methodics),
    path('description/results_control/', views.results_control),
    path('description/advices/', views.advices),
    path('admin/', admin.site.urls),
    path('table/', include('table.urls'), name='table'),
    path('about_user/', views.about_user, name='about_user'),
    path('about/', views.about, name='about_trainer'),
    path('registration/', include('table.urls'), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
]
