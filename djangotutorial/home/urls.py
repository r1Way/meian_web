from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("findmeian/", views.findmeian, name="findmeian"),
    path("about/", views.about, name="about"),
]