"""merchandise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from frontend.views import IndexView

urlpatterns = [
    url(r'^item/',
        include('item.urls',
                namespace='item')),
    url(r'^supply/',
        include('supply.urls',
                namespace='supply')),
    url(r'^admin/', 
        admin.site.urls),
    url(r'^login/$', 
        auth_views.login, 
        name='login'),
    url(r'^$', 
        IndexView.as_view(), 
        name='index'),
    url(r'^users/', include('schedule.urls', namespace='users', app_name='schedule')),

    url(r'^location/', include('location.urls', namespace='location', app_name='location')),
]
