from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', views.editUser, name='edit'),
    url(r'^blog/(?P<user_id>\d+)/$', views.userBlog, name='blog'),
]
