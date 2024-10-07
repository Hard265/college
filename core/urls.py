from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("examination_results/", views.examination_results,
         name="examination_results")
]
