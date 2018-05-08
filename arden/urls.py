from django.urls import re_path

from arden import views

urlpatterns = [
    re_path(r'^upo', views.appendUpo),
]
