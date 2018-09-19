from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from news import views


urlpatterns = [
    url(r'news/$', views.read_news, name="read_news"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),

]
