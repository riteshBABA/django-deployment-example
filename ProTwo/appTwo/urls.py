from django.urls import path
from . import views


app_name = 'appTwo'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'), 
]
