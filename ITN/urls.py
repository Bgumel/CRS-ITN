from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from ninja import NinjaAPI, Redoc
from .api import router as itn_router




urlpatterns = [
    path("", views.Index, name="index"), #home page
    path("register/", views.register, name="register"), #user registration
    path("accounts/", include("django.contrib.auth.urls")), #authentication
    path('itn-distribution/', views.itn_distribution_view, name='itn_distribution_form'),
    path('itn-distribution-success/', views.itn_distribution_success, name='itn_distribution_success'),
    path('distributions/', views.distributions, name='distributions'),
     path('support/', views.support, name='support'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    

    

    
] 
