from django.urls import path

from . import views 


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]

