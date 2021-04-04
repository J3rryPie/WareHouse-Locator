from django.urls import path,include
from . import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',user_views.home,name='user-home'),
    path('signup/',user_views.signup,name='signup'),
    path('about/',user_views.about,name='about-us'),
    path('project/',user_views.project,name='about-project'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('cities/',user_views.all_cities_view,name='all_cities'),
    path('input/',user_views.input_view,name='input'),
    path('output/',user_views.input_view,name='output'),
]