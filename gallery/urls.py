from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^location/(?P<location>\w+)/', views.get_image_location, name='location'),
]