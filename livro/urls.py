from django.urls import path
from . import views

urlpatterns = [
   path('', views.aggregate_annotate, name='aggregate_annotate')
]
