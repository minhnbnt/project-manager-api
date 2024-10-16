from django.urls import path, include

from .views import hello

urlpatterns = [
    path("hello/", hello),
    path("users/", include("api.users.urls")),
    path("projects/", include("api.projects.urls")),
    path("invitations/", include("api.invitations.urls")),
]
