"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from goms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index.html', views.index, name='index'),
    path('elements.html', views.elements, name='elements'),
    path('generic.html', views.generic, name='generic'),
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
    path('useraddimpl', views.useraddimpl, name='useraddimpl'),
    path('machine.html', views.machine, name='machine'),

    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('logout', views.logout, name='logout'),
    path('userinfo', views.userinfo, name='userinfo'),
    path('userdelete', views.userdelete, name='userdelete'),
    path('userupdate', views.userupdate, name='userupdate'),
    path('userupdateimpl', views.userupdateimpl, name='userupdateimpl'),
    path('formimpl', views.formimpl, name='formimpl'),
    path('result.html', views.result, name='result'),

    path('datalist', views.datalist, name='datalist'),
    path('datadelete', views.datadelete, name='datadelete'),

]
