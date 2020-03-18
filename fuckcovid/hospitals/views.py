from .models import Region, Hospital, Resource, Need
from .serializers import *
from rest_framework import generics


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class HospitalList(generics.ListCreateAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        return Hospital.objects.filter(region__pk = self.kwargs['pk'])


class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class NeedList(generics.ListCreateAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

class NeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer
