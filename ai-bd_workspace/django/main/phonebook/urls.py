from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('add/',views.phoneAdd),
    path('delete/',views.phoneDelete),
    path('detail/<int:userId>/',views.phoneDetail),
    path('update/',views.phoneUpdate),

]
