from django.urls import path
from .views import landingPage,blogTable,blogForm,todayBlog


urlpatterns = [
    path('',landingPage),
    path('all-blogs/',blogTable),
    path('blog-form/',blogForm),
    path('today-blogs/',todayBlog),
]