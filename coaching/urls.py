from django.urls import path

from . import views

urlpatterns = [
    # /coaching/
    path('', views.index, name='index'),
]