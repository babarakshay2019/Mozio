from rest_framework import serializers
from .models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('url', 'name', 'email',
                  'language', 'currency',
                  'language', 'phone_number')


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('url', 'provider', 'name', 'price', 'area', 'mpoly')
