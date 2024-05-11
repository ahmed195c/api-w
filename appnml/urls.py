from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('homepage', views.homepage , name="homepage"),
    path('savepro' , views.saveuser , name="saveuser"),
    path('loadusers' ,views.loadusers, name="loadsers"),
    # Additional URL patterns go here
]