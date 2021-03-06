from django.urls import re_path

from arden import views

urlpatterns = [
    re_path(r'^appendUpo/$', views.appendUpo),
    re_path(r'^list/$', views.listUpo),
    re_path(r'^manage_list/$', views.listUpo),
    re_path(r'^listUpo/$', views.listUpo),
    re_path(r'^approve/$', views.approve),
    re_path(r'^collect/$', views.collect),
    re_path(r'^reject/$', views.reject),
    re_path(r'^remove/$', views.remove),
    re_path(r'^show/$', views.show),
    re_path(r'^(?P<name>\w+)_page/$', views.mapz),
]
