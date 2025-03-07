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
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index,login_view,logout_view,sa_dashboard,add_property_owner,ResetPasswordView
from property_owner.views import property_unit_view,lease_agreement_view,property_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Default route for the index page
    path('superadmin/', sa_dashboard, name='sa_dashboard'),
    path('superadmin/add_property_owner/', add_property_owner, name='add_property_owner'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('property_owner/', property_view, name='property_owner'),
    path('property_unit/', property_unit_view, name = "property_unit"),
    path('lease_agreement/', lease_agreement_view, name='lease_agreement'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
