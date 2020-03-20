from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from fuckcovid.hospitals.models import Region
from fuckcovid.makers.models import Maker


class RegionList(ListView):
    queryset = Region.objects.all().order_by('name')
    context_object_name = 'regions'
    template_name = 'makers/region_list.html'


class RegionDetail(DetailView   ):
    template_name = 'makers/region_detail.html'
    context_object_name = 'region'
    model = Region

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['makers'] = self.object.maker_set.order_by('name')
        return context


class MakerDetail(DetailView):
    template_name = 'makers/maker_detail.html'
    context_object_name = 'maker'
    model = Maker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productions'] = self.object.production_set.order_by('resource__name')
        return context

