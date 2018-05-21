from django.urls import re_path

from arden import views

urlpatterns = [
    re_path(r'^appendUpo', views.appendUpo),
    re_path(r'^success', views.success),
]
