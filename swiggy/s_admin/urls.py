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
    path('update_area/',views.update_area,name='update_area'),
    path('update_area_data/',views.update_area_data,name='update_area_data'),
    path('delete_area/',views.delete_area,name='delete_area'),

    #Type#
    path('open_type/',views.open_type.as_view(),name='open_type'),
    path('update_type/',views.update_type,name='update_type'),
    path('update_type_data/',views.update_type_data,name='update_type_data'),
    path('delete_type/',views.delete_type,name='delete_type'),

    #Restaurant#
    path('restro_menu/',views.restro_menu,name='restro_menu'),
    path('pending_restro/',views.pending_restro,name='pending_restro'),
    path('rejected_restro/',views.rejected_restro,name='rejected_restro'),
    path('show_rejected_restro/',views.show_rejected_restro,name='show_rejected_restro'),
    path('approved_restro/',views.approved_restro,name='approved_restro'),
    path('show_accepted_restro/',views.show_accepted_restro,name='show_accepted_restro')
]
