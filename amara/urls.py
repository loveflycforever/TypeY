from django.urls import re_path

from amara import views

urlpatterns = [
    re_path('$', views.oo),
]
