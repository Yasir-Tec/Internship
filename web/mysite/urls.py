from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('regpage/', views.UserRegPage, name="render UserRegPage"),
    path('regpage/UserRegistered/', views.UserRegistered, name="user registered "),
    path('userLoginPage/', views.UserLoginPage, name="user Login Page"),
    path('userLoginPage/UserLogin/', views.AuthUser, name="Authenticate the  user ")

]
