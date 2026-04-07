from django.urls import path
from . import views

app_name = "database_manager"

urlpatterns = [
    path("", views.index, name="index"),
    path("coil/<int:pk>/", views.coil_detail, name="coil_detail"),
    path("holding-register/<int:pk>/", views.holding_register_detail, name="holding_register_detail"),
]
