from django.contrib import admin
from django.urls import path, include

# Here app urls are included
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
