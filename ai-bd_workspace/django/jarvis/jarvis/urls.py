# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

# Custom error handlers
handler404 = 'jarvis.views.custom_404_view'
handler500 = 'jarvis.views.custom_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
]
