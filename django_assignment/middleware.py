from django.shortcuts import redirect
from templates.views import blog_form,detail_of_blog

class MyCustomMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func, view_args,view_kwargs):
        if request.user:
            if not request.user.is_authenticated and view_func ==blog_form:
                    return redirect('/login/')
                
            if not request.user.is_authenticated and view_func ==detail_of_blog:
                    return redirect('/login/')

                #