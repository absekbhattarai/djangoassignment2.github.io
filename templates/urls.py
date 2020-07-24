from django.urls import path
from .views import landing_page,blog_table,blog_form,today_blog,register_form,user_login,select_login,user_logout,user_profile,detail_of_blog,edit_user_profile,edit_user_profile


urlpatterns = [
    path('',landing_page),
    path('all-blogs/',blog_table),
    path('blog-form/',blog_form),
    path('today-blogs/',today_blog),
    path('register/',register_form),
    path('login/',user_login),
    path('select-login/',select_login),
    path('logout/',user_logout),
    path('profile/',user_profile),
    path('detail/<int:user_id>',detail_of_blog),
    path('profile/edit-profile/<int:user_id>',edit_user_profile),

]