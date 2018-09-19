from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from news import views


urlpatterns = [
    url(r'^news/$', views.read_news, name="read_news"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^create/$', views.create_news, name="create_news"),
    url(r'^delete/(?P<slug>[0-9A-Za-z_\-]+)/$', views.delete_news, name="delete_news"),
    url(r'^save/$', views.save_news, name="save_news"),
]
