"""
URL configuration for myhtml project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myhtml import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.main),
    path("test1/", views.test1),
    path("quiz1/", views.quiz1),
    path("test2/", views.test2),
    path("quiz2/", views.quiz2),
    path("test3/", views.test3),
    path("test4/", views.test4),
    path("quiz3/", views.quiz3),
    path("quiz4/", views.quiz4),


]
