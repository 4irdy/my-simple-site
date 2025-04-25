from django.contrib import admin
from django.urls import path, include  # 👈 include is already imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # 👈 connects your main app
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ ADD THIS LINE
]
