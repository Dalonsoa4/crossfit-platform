from django.urls import path
from . import views


urlpatterns = [
    path(
        "inscription/",
        views.visitor_registration,
        name="visitor_registration"
    ),

    path(
        "inscription/confirmation/",
        views.registration_success,
        name="registration_success"
    ),
]