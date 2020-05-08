"""swiggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant_log_reg/',views.restaurant_log_reg,name='restaurant_log_reg'),
    path('restaurant_login/',views.restaurant_login,name='restaurant_login'),
    path('restaurant_registration/',views.restaurant_registration,name='restaurant_registration'),
    path('restaurant_registration_saved/',views.restaurant_registration_saved,name='restaurant_registration_saved'),
    path('restaurant_login_saved/',views.restaurant_login_saved,name='restaurant_login_saved'),


    #forget password#

    path('forget_password_page/',views.forget_password_page,name='forget_password_page'),
    path('reset_password_email/',views.reset_password_email,name='reset_password_email'),
    path('otp_validate/',views.otp_validate,name='otp_validate'),
    path('reset_password_conformation/',views.reset_password_conformation,name='reset_password_conformation')

]
