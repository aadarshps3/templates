from django.urls import path

from homeapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('adminpage',views.adminpage,name='adminpage'),
]