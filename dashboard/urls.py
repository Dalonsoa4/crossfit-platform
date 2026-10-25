from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path(
        "",
        views.dashboard_home,
        name="dashboard_home"
    ),

    path(
        "connexion/",
        auth_views.LoginView.as_view(
            template_name="dashboard/login.html",
            redirect_authenticated_user=True
        ),
        name="dashboard_login"
    ),

    path(
        "deconnexion/",
        auth_views.LogoutView.as_view(),
        name="dashboard_logout"
    ),

    path(
    "visiteurs/",
    views.visitor_list,
    name="visitor_list"
    ),

    path(
    "visiteurs/<int:visitor_id>/",
    views.visitor_detail,
    name="visitor_detail"
    ),
]