from django.urls import path, include
from django.contrib import admin
from .feed import LatestEntriesFeed
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.getstarted , name='getstarted'),
    path('uchiha/login/',views.login_view,name='userlogin'),
    path('uchiha/signup/',views.register_view,name='usersignup'),
    path('uchiha/logout/',views.logout_view,name='userlogout'),
    path('uchiha/upload/', views.upload, name='upload'),
    path('uchiha/download/',views.download,name='download'),
    path('uchiha/profile/',views.profile,name='profile'),
    path('uchiha/search/',views.search,name='search'),
    path('uchiha/comment/', LatestEntriesFeed()),
    path('uchiha/comment/',views.comm,name='comm')
]