from django.urls import re_path

from arden import views

urlpatterns = [
    re_path(r'^appendUpo', views.appendUpo),
    re_path(r'^listUpo', views.listUpo),
    re_path(r'^collectUpoInfo', views.collect),
    re_path(r'^approve', views.approve),
    re_path(r'^reject', views.reject),
]
