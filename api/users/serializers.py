from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers

from api.models import Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, password: str):
        try:
            validate_password(password)
            return password

        except exceptions.ValidationError as e:
            raise serializers.ValidationError(e.messages)

    def create(self, validated_data: dict):
        registered_user = User.objects.create_user(**validated_data)
        Project.objects.create(
            title=f"{registered_user.username.title()} Project",
            description="This is a personal project root.",
            # Có thể để None hoặc đặt giá trị mặc định khác
            time_start=None,
            time_end=None,
            type="personal",
            owner=registered_user,
            parent=None,  # Đây là root project nên parent là None
        )

        return registered_user
