from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import (
    ProjectDetailSerializer,
    ProjectListSerializer,
)


class ProjectListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectListSerializer

        return ProjectDetailSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectDetailSerializer

    queryset = Project.objects.all()
    lookup_field = "id"
