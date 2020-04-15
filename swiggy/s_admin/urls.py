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

from s_admin import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.Homepage,name='main'),
    path('admin_login/',views.admin_login.as_view(),name='admin_login'),
    path('admin_body_page/',views.admin_body_page,name='admin_body_page'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),

    #state#
    path('open_state/',views.open_state.as_view(),name='open_state'),
    path('update_state/',views.update_state,name='update_state'),
    path('update_state_data/',views.update_state_data,name='update_state_data'),
    path('delete_state/',views.delete_state,name='delete_state'),

    #city#
    path('open_city/',views.open_city.as_view(),name='open_city'),
    path('update_city/',views.update_city,name='update_city'),
    path('update_city_data/',views.update_city_data,name='update_city_data'),
    path('delete_city/',views.delete_city,name='delete_city'),

    #Area#
    path('open_area/',views.open_area.as_view(),name='open_area'),
    path('delete_area/',views.delete_area,name='delete_area')
]