from django.forms import ModelForm
from .models import blogDetails,authorDetails



class MyFormBlog(ModelForm):
    class Meta:
        model = blogDetails
        fields = ['title','blog']

class MyAuthor(ModelForm):
    class Meta:
        model = authorDetails
        fields = ['name','email']