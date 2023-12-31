from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gino", views.gino, name="gino"),
    path("<str:name>", views.greet, name="greet")
]