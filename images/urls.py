from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^create/$', views.image_create, name='create'),
               url(r'^detail/(?P<image_id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
               url(r'^like/$', views.image_like, name='like'),
               url(r'^$', views.image_list, name='list'),
               url(r'^(?P<username>[-\w]+)/$', views.image_list, name='user_image_list'),
               url(r'^(?P<username>[-\w]+)/like/$', views.images_liked, name='images_liked'),
]