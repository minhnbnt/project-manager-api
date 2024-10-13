from django.urls import path
from .views import ProjectDetailView, ProjectListView

urlpatterns = [
    path("", ProjectListView.as_view()),
    path("<str:id>", ProjectDetailView.as_view()),
]
