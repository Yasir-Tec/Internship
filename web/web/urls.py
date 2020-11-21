from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Softtech Admin"
admin.site.site_title = "Softtech Admin Portal"
admin.site.index_title = "Welcome to Softtech"

urlpatterns = [
    path('', include('mysite.urls')),
    path('admin/', admin.site.urls),
]
