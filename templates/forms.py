from django.forms import ModelForm
from .models import blog_Details,author_Details



class MyFormBlog(ModelForm):
    class Meta:
        model = blog_Details
        fields = ['title','blog']

class MyAuthor(ModelForm):
    class Meta:
        model = author_Details
        fields = ['name','email']