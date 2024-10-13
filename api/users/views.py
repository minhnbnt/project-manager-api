from rest_framework import generics

from .serializers import UserSerializer


class UserRegister(generics.CreateAPIView):
    """
    Method POST: Tạo user mới
    """

    serializer_class = UserSerializer
