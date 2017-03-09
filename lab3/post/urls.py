from django.conf.urls import url
from .import views

urlpatterns = [
   # url(r'^$', views.index, name='index'),
    url(r'^create/', views.createPost, name='create'),
    url(r'^remove/(?P<post_id>\d+)/$', views.removePost, name='remove'),
    url(r'^edit/(?P<post_id>\d+)/', views.editPost, name='edit'),
]
