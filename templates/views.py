from django import template
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserChangeForm
from datetime import date
from .forms import MyFormBlog
from .login_register import Register, UserInfoForm,EditProfileBio,EditUserProfile
from .models import BlogDetails, UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth



def landing_page(request):
    return render(request, "templates/landing.html",{'pageTitle': 'Homepage'})

def select_login(request):
    return render(request,"templates/select-login.html",{'pageTitle':'Select Login'})

def register_form(request):
    registered = False
    user_details = Register() #username, pass, email
    bio_details = UserInfoForm() #name , dob
    
    
    if request.method == 'POST':
        user_details = Register(request.POST)
        bio_details = UserInfoForm(request.POST)
        
        if user_details.is_valid() and bio_details.is_valid():
            user_instance = user_details.save()
            user_instance.set_password(user_instance.password)
            user_instance.save()
            profile = bio_details.save(commit=False)
            profile.user = user_instance
            profile.save()
            registered = True
            return  redirect('/login/')

        else:
            print(user_details.errors,bio_details.errors)

    return render(request,'templates/register.html',
                  {'user_details':user_details,'bio_details':bio_details,'pageTitle':'Register Form'})





def user_logout(request):
    logout(request)
    return redirect('/homepage/')

def user_login(request):
    blog_table = BlogDetails.objects.all()
    author_table = UserInfo.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/all-blogs')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Login Failed.")
            print("They used username: {} and password: {}".format(username,password))
            html ="Invalid login details given.Click"+'<a href="/register/">here</a>'+"to register."
            return HttpResponse(html)
    elif request.method=='GET':
        return render(request, 'templates/login.html',{})

@login_required
def user_profile(request):
    loggedin_user = request.user
    blog_table = BlogDetails.objects.filter(author_username = loggedin_user)
    user_profile = UserInfo.objects.get(user = request.user)
    return render(request,'templates/profile.html',{'pageTitle':'Your Profile','user_profile':user_profile,'blogTable':blog_table})

def blog_table(request):
    blog_table = BlogDetails.objects.all()
    return render(request, "templates/blog-table.html",{'pageTitle': 'All Blogs','blogTable':blog_table})
    

def today_blog(request):
    today = date.today()
    today_blog_table = BlogDetails.objects.filter(posted_at=today)
    today_author_table = UserInfo.objects.all()
    return render(request, "templates/today-blog.html",{'pageTitle': 'Today Blogs','todayauthorTable': today_author_table,'todayblogTable':today_blog_table})


def blog_form(request):
    blog_form = MyFormBlog()
    if request.method == 'POST':
        blogForm = MyFormBlog(request.POST)
        
        if blogForm.is_valid():
            blog_instance = blogForm.save(commit=False)
            blog_instance.author_username = request.user
            blogForm.save()
            return redirect('/homepage/all-blogs/')
        else:
            return HttpResponse("something went wrong")
    return render(request, "templates/blog-form.html",{'pageTitle': 'Write a Form','blogForm':blog_form})


@login_required
def detail_of_blog(request,user_id):
    detail_obj = get_object_or_404(BlogDetails,id = user_id)
    return render(request,'templates/details.html',{'detail_obj':detail_obj,'pageTitle':'Detail Blog'})

@login_required
def edit_user_profile(request):
    # user_object =get_object_or_404(UserInfo,id=user_id) 
    # 
    #     user_form = EditProfileBio(request.POST,instance=user_object)
       
    #     if user_form.is_valid :
    #         user_form.save()
    #         request.user.save()
    #         return redirect('/homepage/profile/')
    #     else:
    #         return HttpResponse("something went wrong")
    # else:
    #     user_form = EditProfileBio(instance=user_object)
    if request.method == 'POST':
        
        user_form = EditUserProfile(request.POST,instance=request.user)
        bio_form = EditProfileBio(request.POST)
        if user_form.is_valid and bio_form.is_valid:
            user_form.save()
            bio_instance = bio_form.save(commit=False)
            bio_instance.user_id = request.user.id
            bio_instance.save()
            return redirect('/homepage/profile/')
        else:
            return HttpResponse("something went wrong")
    else:
        user_form = EditUserProfile(instance=request.user)
        bio_object = UserInfo.objects.filter(user_id=request.user.id).values()
        print(bio_object)
        
        return render(request,'templates/edit-profile.html',{'user_form':user_form,'bio_object':bio_object})


@login_required
def edit_blog(request,blog_id):
    blog_object = get_object_or_404(BlogDetails,id = blog_id)
    form_id = blog_id
    if request.method == "POST":
        blog_form = MyFormBlog(request.POST,instance=blog_object)
        print(blog_form)
        if blog_form.is_valid():
            blog_instance = blog_form.save(commit=False)
            blog_instance.save()
            return redirect('/homepage/profile/')
        else:
            return HttpResponse("something went wrong")

   
    blog_form = MyFormBlog(instance=blog_object)
    return render(request,'templates/edit-form.html',{'blogForm':blog_form,'form_id':form_id})

@login_required
def delete_blog(request,form_id):
     blog_object = BlogDetails.objects.get(id = form_id)
     blog_object.delete()
     return redirect('/homepage/profile/')
