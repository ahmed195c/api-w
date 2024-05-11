from django.urls import path

from . import views

urlpaterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name="login"),
]