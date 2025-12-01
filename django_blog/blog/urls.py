from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('post/create/', views.post_create, name = 'post_create'),
    path('post/<slug:slug>/', views.post_detail, name = 'post')
]
