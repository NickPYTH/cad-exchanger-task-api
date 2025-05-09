from django.urls import path

from .views import generate_simple_response

urlpatterns = [
    path('generate_simple_response', generate_simple_response),
]
