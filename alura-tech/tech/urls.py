from django.urls import path
from tech import views

urlpatterns = [
    path('', views.index, name='index'),
]