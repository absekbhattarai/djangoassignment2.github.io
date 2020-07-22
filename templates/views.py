from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .forms import MyFormBlog, MyAuthor
from .models import blog_Details,author_Details



def landingPage(request):
    return render(request, "templates/landing.html",{'pageTitle': 'Homepage'})


def blogTable(request):
    blogTable = blog_Details.objects.all()
    authorTable = author_Details.objects.all()
    return render(request, "templates/blog-table.html",{'pageTitle': 'All Blogs','blogTable':blogTable,'authorTable':authorTable})
    

def todayBlog(request):
    today = date.today()
    todayblogTable = blog_Details.objects.filter(posted_at=today)
    todayauthorTable = author_Details.objects.all()
    return render(request, "templates/today-blog.html",{'pageTitle': 'Today Blogs','todayauthorTable': todayauthorTable,'todayblogTable':todayblogTable})


def blogForm(request):
    blogForm = MyFormBlog()
    authorForm = MyAuthor()
    if request.method == 'POST':
        blogForm = MyFormBlog(request.POST)
        authorForm = MyAuthor(request.POST)
        if blogForm.is_valid() and authorForm.is_valid():
            instance = authorForm.save()
            blog_instance = blogForm.save(commit=False)
            blog_instance.authorEmail = instance
            blogForm.save()
            return redirect('/homepage/all-blogs/')
        else:
            return HttpResponse("something went wrong")
    return render(request, "templates/blog-form.html",{'pageTitle': 'Write a Form','blogForm':blogForm,'authorForm':authorForm})




