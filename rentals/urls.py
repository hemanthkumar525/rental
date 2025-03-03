"""
URL configuration for rentals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .views import index,login_view,logout_view,sa_dashboard,add_property_owner


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Default route for the index page
    path('superadmin/', sa_dashboard, name='sa_dashboard'),
    path('superadmin/add_property_owner/', add_property_owner, name='add_property_owner'),
    path('property_owner/', include('property_owner.urls'), name='property_owner'),  
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
