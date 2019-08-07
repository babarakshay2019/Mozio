from rest_framework import viewsets, generics
from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer
from django.contrib.gis.geos import Point


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Provider Operations
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    ServiceArea Operations
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaList(generics.ListAPIView):
    """
    A ListApiView to search area.
    """
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        lat = self.request.GET.get('lat')
        lon = self.request.GET.get('lon')
        pnt_wkt = Point(float(lat), float(lon))
        return ServiceArea.objects.filter(mpoly__intersects=pnt_wkt)
