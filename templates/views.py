from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .forms import MyFormBlog
from .models import blogDetails,authorDetails



def landingPage(request):
    return render(request, "templates/landing.html",{'pageTitle': 'Homepage'})


def blogTable(request):
    blogTable = blogDetails.objects.all()
    authorTable = authorDetails.objects.all()
    return render(request, "templates/blog-table.html",{'pageTitle': 'All Blogs','blogTable':blogTable,'authorTable':authorTable})
    

def todayBlog(request):
    today = date.today()
    todayblogTable = blogDetails.objects.filter(posted_at=today)
    todayauthorTable = authorDetails.objects.all()
    return render(request, "templates/today-blog.html",{'pageTitle': 'Today Blogs','todayauthorTable': todayauthorTable,'todayblogTable':todayblogTable})


def blogForm(request):
    blogForm = MyFormBlog()
    
    if request.method == 'POST':

        blogForm = MyFormBlog(request.POST)
        
       
        
        if blogForm.is_valid():
            blogForm.save()
            return redirect('/homepage/all-blogs/')
        else:
            return HttpResponse("something went wrong")
    return render(request, "templates/blog-form.html",{'pageTitle': 'Write a Form','blogForm':blogForm})




