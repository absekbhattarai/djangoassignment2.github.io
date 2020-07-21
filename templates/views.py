from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .forms import MyFormBlog, MyAuthor
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
    authorForm = MyAuthor()
    if request.method == 'POST':
        blogForm = MyFormBlog(request.POST)
        authorForm = MyAuthor(request.POST)
        if blogForm.is_valid() and authorForm.is_valid():
            instance = authorForm.save()
            instance1 = instance.email # instance1 gets the email that to be saved in the blogDetails
            # blogForm.save(commit=False)
            # blogForm.authorEmail = instance1  -> Here as I haven't included "authorEmail" in forms i.e. blogForm
            # blogForm.save()


            
            return redirect('/homepage/all-blogs/')
        else:
            return HttpResponse("something went wrong")
    return render(request, "templates/blog-form.html",{'pageTitle': 'Write a Form','blogForm':blogForm,'authorForm':authorForm})




