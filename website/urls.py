from django.conf.urls import url, include
from website import views


urlpatterns = [
    url(r'^home/$', views.landing_page, name="homepage"),
    url(r'', views.landing_page),
]
