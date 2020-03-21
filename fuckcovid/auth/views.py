from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import UpdateView, DetailView

from fuckcovid.auth.models import User, Profile
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ProfileDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['name', 'surname', 'company', 'address', 'phone', 'city', 'country']

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse('auth:profile-detail')
