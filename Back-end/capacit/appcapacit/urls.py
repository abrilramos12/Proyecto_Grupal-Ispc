from django.urls import path, re_path, include
from django.urls import re_path as url
from . import views

from .views import LoginView, LogoutView

urlpatterns: [
    url(r"^user$", views.UserList.as_view()),
    url(r"user/(?P<pk>[0-9]+)$", views.UserDetail.as_view()),

    path("auth/login",
         LoginView.as_view(), name="auth_login"),

    path("auth/logout",
         LogoutView.as_view(), name="auth_logout"),     



]


    