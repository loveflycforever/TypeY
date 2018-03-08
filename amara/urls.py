from django.urls import re_path, path

from amara import views

urlpatterns = [
    re_path(r'^collection', views.dealCollections),
    re_path(r'^initialization', views.dealInitialization),
    # re_path('$', views.requestInfo),
]
