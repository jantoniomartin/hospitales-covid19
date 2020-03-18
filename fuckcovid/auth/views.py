from fuckcovid.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing and retrieving users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
