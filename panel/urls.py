from django.urls import include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from panel.settings import LOGIN_URL 
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^register/$', views.register),
    re_path(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(next_page=LOGIN_URL), name='logout'),
    re_path(r'^dashboard/', include('dashboard.urls')),
    re_path(r'^website/', include('website.urls')),
    re_path(r'^database/', include('database.urls')),
    re_path(r'^setting/', include('setting.urls')),
    re_path(r'^ftp/', include('ftp.urls')),
    re_path(r'^crontab/', include('crontab.urls')),
]
