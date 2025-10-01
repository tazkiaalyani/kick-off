from django.contrib import admin
from django.urls import path
from django.urls import path, include
from main.views import edit_product

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
