from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^delete-action/$', views.delete_action, name='delete_action'),
]