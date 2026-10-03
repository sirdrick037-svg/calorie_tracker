"""
URL configuration for calorie_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from calories import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path( "",views.home,name="home"),
    path("add/",views.add_food,name="add_food"),
    path("edit/<int:food_id>/",views.edit_food,name="edit_food"),
    path("delete/<int:food_id>/",views.delete_food,name="delete_food"),
    path("reset/",views.reset_today,name="reset_today"),
]
