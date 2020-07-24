from django.forms import ModelForm
from .models import BlogDetails



class MyFormBlog(ModelForm):
    class Meta:
        model = BlogDetails
        fields = ['title','blog']
