from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^Den/', views.Den, name='Den'),
    url(r'^sales/', views.sales, name='sales'),
    url(r'^news/', views.news, name='news'),
]

