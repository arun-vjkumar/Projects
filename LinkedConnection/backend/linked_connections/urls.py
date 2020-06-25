from django.contrib import admin
from django.urls import path

from linked_connections import views

urlpatterns = [
    path('initialize', views.LinkedConnections.initialize_data),
    path('connections', views.LinkedConnections.get_all_connections),
    path('userConnections', views.LinkedConnections.get_user_connections),
    path('connectionByNameLocation', views.LinkedConnections.get_connections_by_name_loc)
]
