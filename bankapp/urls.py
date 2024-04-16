from django.urls import path
from bankapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('appln',views.appln,name='appln'),
    path('appln_btn',views.appln_btn,name='appln_btn'),
    path('home',views.home,name='home'),
    path('cities', views.cities, name="cities"),
]
