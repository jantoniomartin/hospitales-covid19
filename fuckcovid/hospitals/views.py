from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Region, Hospital, Resource, Need
from .serializers import *
from rest_framework import generics

class Home(TemplateView):
    template_name = 'hospitals/home.html'


class RegionList(ListView):
    queryset = Region.objects.all().order_by('name')
    context_object_name = 'regions'
    template_name = 'hospitals/region_list.html'


class RegionDetail(DetailView   ):
    template_name = 'hospitals/region_detail.html'
    context_object_name = 'region'
    model = Region

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospitals'] = self.object.hospital_set.order_by('name')
        return context


class HospitalDetail(DetailView):
    template_name = 'hospitals/hospital_detail.html'
    context_object_name = 'hospital'
    model = Hospital

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['needs'] = self.object.need_set.order_by('resource__name')
        return context


class HospitalAddNeed(CreateView):
    model = Need
    fields = ['resource', 'amount_per_day', 'comment']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = get_object_or_404(Hospital, pk=self.kwargs['pk'])
        context['prev_url'] = self.request.path
        return context

    def form_valid(self, form):
        form.instance.hospital = get_object_or_404(Hospital, pk=self.kwargs['pk'])
        form.instance.editor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('hospitals:hospital-detail', args=[self.kwargs['pk']])


class NeedUpdateView(UpdateView):
    model = Need
    fields = ['amount_per_day', 'comment']

    def get_success_url(self):
        return reverse('hospitals:hospital-detail', args=[str(self.object.hospital.pk)])


class ResourceCreateView(CreateView):
    model = Resource
    fields = ['name', ]

    def get_success_url(self):
        return self.request.GET.get('next')

class ResourceDetail(DetailView):
    template_name = 'hospitals/resource_detail.html'
    context_object_name = 'resource'
    model = Resource

class NeedList(generics.ListCreateAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

class NeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer
