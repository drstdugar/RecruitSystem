from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('category', views.category, name='category'),
    path('jobs', views.jobs, name='jobs')
]
