from django.urls import path

from . import views


urlpatterns = [
        path("user", views.user, name = "user"),
        path("login", views.login_view, name="login"),
        path("logout", views.logout_view, name="logout"),


]