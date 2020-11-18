from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mysite/', include('mysite.urls')),
    path('admin/', admin.site.urls),
]