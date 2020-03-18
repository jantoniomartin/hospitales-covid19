from .models import Region, Hospital, Resource, Need
from rest_framework import serializers


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['pk',
                  'name']


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = ['pk',
                  'city',
                  'phone',
                  'name',
                  'address',
                  'region',
                  'comment',
                  ]
        extra_kwargs = {
            'region': {'view_name': 'hospitals:region-detail'}
        }


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['pk',
                  'name',
                  ]


class NeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Need
        fields = ['pk',
                  'hospital',
                  'resource',
                  'amount_per_day',
                  'comment',
                  'editor',
                  'updated_at',
                  ]
        extra_kwargs = {
            'hospital': {'view_name': 'hospitals:hospital-detail'},
            'resource': {'view_name': 'hospitals:resource-detail'},
            'editor': {'view_name': 'auth:user-detail'},
        }
