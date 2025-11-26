from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path("under-construction/", views.UnderConstruction.as_view(), name="under_construction"),
]