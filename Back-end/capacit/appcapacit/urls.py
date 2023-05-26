from django.urls import path, re_path
from django.urls import re_path as url

from . import views

urlpatterns: [
    url(r"^user$", views.UserList.as_view()),
    url(r"user/(?P<pk>[0-9]+)$", views.UserDetail.as_view())


]
    