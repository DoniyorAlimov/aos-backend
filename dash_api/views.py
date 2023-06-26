from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Aggregation
from .serializers import AggregationSerializer


class AggregationViewSet(ModelViewSet):
    http_method_names = ['get']

    queryset = Aggregation.objects.select_related(
        'equipment').select_related('aggregation_type').all()
    serializer_class = AggregationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['equipment', 'aggregation_type']
    ordering_fields = ['timestamp']
