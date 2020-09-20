from django.urls import path
from . import views

urlpatterns = [
    path('apply', views.apply, name='apply'),
    path('add_apply', views.add_apply, name='add_apply'),
    path('infoview', views.infoview, name='infoview'),
]
