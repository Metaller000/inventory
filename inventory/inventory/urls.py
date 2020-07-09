from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('inventory/', include('main.urls')), 
    path('admin/', admin.site.urls),
]