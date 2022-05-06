from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Core App
    path('', include('core.urls', namespace='core')),
    
    path('admin/', admin.site.urls),
]
