from django.forms import ModelForm
from .models import blogDetails



class MyFormBlog(ModelForm):
    class Meta:
        model = blogDetails
        fields = ['title','blog','name','email1']

