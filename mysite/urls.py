from django.contrib import admin
from django.urls import path, include  # 👈 add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # 👈 this connects your app's URLs
]
