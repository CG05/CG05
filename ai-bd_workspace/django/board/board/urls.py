"""
URL configuration for board project.

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
from board import views
from test1 import views as t1views
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("chart/", views.chartMain),
    re_path(r"chart/weekly/(\d*)", views.chartWeekly),
    re_path(r"chart/month/(\d*)", views.chartMonth),
    re_path(r"chart/year/(19[8-9][0-9]|20[0-1][0-9]|202[0-4])", views.chartYear),
    # path("chart/test1/", t1views.main),
    path("chart/test1/", include('test1.urls')),
]

# url : chart/
# - 차트 페이지 입니다.
# url : chart/weekly/1~52
# - 1 주 차트 페이지 입니다
# - 52 주 차트 페이지 입니다
# - 53 주 차트 페이지는 없습니다

# url : chart/month/1~12
# - 1 월 차트 페이지 입니다
# - 12 월 차트 페이지 입니다
# - 13 월 차트 페이지는 없습니다
 
