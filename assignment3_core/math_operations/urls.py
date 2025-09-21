from django.urls import path
from . import views

urlpatterns = [
    path("", views.math_form, name="math_form"),
]
