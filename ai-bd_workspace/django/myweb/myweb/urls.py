"""
URL configuration for myweb project.

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
from django.urls import path, re_path
from myweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    # pattern의 속성을 지정하지 않으면 str
    path('pattern1/<name>/', views.pattern1),
    path('pattern2/<int:name>/', views.pattern2),
    path('pattern3/<slug:name>/', views.pattern3),
    path('quiz1/<lang>', views.quiz1),
    re_path(r'^pattern4/?(ko|en|jp)/$', views.pattern4),
    re_path(r'^regex1/...(...)',views.regex1),
    re_path(r'^abc.*/',views.regex2),
    re_path(r'.*cba$',views.regex3),
    re_path(r'regex4/*',views.regex4),
    re_path(r'regex5/(.+)',views.regex5),
    re_path(r'regex6/([0-9]+)/',views.regex6),
    re_path(r'regex7/([0-9a-zA-Zㄱ-힣])/',views.regex7),
    re_path(r'regex8/([0-9]{3}|[a-z]{5}|[ㄱ-힣]{2})/',views.regex8),
    re_path(r'regex9/(.{3,5})/',views.regex9),
    re_path(r'regex10/(\d{3}|\w{3})',views.regex10),

    
    
    
    re_path(r'email/(\w+[@]\w+[.]com|\w+[@]\w+[.]net)',views.email),
    re_path(r'email1/(\w+[@]\w+[.]\w{3}|\w+[@]\w+[.]\w{2}[.]\w{2})',views.email1),

    re_path(r'phone/([0-3]{2,3}-[0-9]{3,4}-[0-9]{4})/',views.phone),

    
    
]

# 문제 1: url패턴 str을 사용하여 이름은 lang으로 하고
# 값이 ko면 "한국어 페이지", 값이 en이면 "영어 페이지", 값이 jp면 "일본어 페이지"라고 출력