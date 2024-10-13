from rest_framework import serializers
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
)

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "type",
            "owner",
            "manager",
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )

    manager = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "time_start",
            "time_end",
            "type",
            "owner",
            "manager",
            "parent",
        )

    def create(self, validated_data: dict):
        request = self.context.get("request")
        if request is None:
            raise AuthenticationFailed()

        owner = request.user
        if owner is None:
            raise NotAuthenticated()

        return Project.objects.create(
            **validated_data,
            owner=owner,
        )
