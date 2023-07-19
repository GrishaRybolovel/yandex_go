from django.urls import path
from .views import time_diagram

urlpatterns = [
    path('', time_diagram, name="time_diagram"),
]