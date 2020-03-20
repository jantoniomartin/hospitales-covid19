from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class HospitalUpdate(LoginRequiredMixin, UpdateView):
    model = Hospital
    fields = ['name', 'city', 'phone', 'address', 'comment']


class HospitalAddNeed(LoginRequiredMixin, CreateView):
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


class NeedUpdateView(LoginRequiredMixin, UpdateView):
    model = Need
    fields = ['amount_per_day', 'comment']

    def get_success_url(self):
        return reverse('hospitals:hospital-detail', args=[str(self.object.hospital.pk)])


class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['name', ]

    def get_success_url(self):
        return self.request.GET.get('next')


class ResourceDetail(DetailView):
    template_name = 'hospitals/resource_detail.html'
    context_object_name = 'resource'
    model = Resource

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_per_day'] = self.object.need_set.aggregate(total_per_day=Sum('amount_per_day'))['total_per_day']
        return context


class ResourceList(ListView):
    template_name = 'hospitals/resource_list.html'
    context_object_name = 'resources'
    model = Resource


class NeedList(generics.ListCreateAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer

class NeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer
