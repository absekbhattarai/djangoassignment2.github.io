from django.urls import path,include
from django.contrib import admin 

urlpatterns = [
    path('homepage/',include('templates.urls')),
    path('',include('templates.urls')),
    path('admin/',admin.site.urls),
]
