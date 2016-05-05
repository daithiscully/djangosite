from django.conf.urls import url
from . import views

#r'^$' is the home page for /music
urlpatterns = [
    url(r'^$', views.index, name='index'),
]