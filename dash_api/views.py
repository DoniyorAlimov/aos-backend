from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Aggregation, Equipment
from .serializers import AggregationSerializer, EquipmentSerializer


class AggregationViewSet(ModelViewSet):
    http_method_names = ['get', 'options', 'head']

    queryset = Aggregation.objects.select_related(
        'equipment').select_related('aggregation_type').all()
    serializer_class = AggregationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['equipment', 'aggregation_type']
    ordering_fields = ['timestamp']


class EquipmentViewSet(ModelViewSet):
    http_method_names = ['get', 'options', 'head']

    serializer_class = EquipmentSerializer

    def get_queryset(self):
        names = self.request.query_params.getlist('name[]')
        aggregation_type = self.request.query_params.get('aggregation_type')

        queryset = Aggregation.objects.select_related(
            'aggregation_type').order_by('timestamp')

        if aggregation_type:
            queryset = queryset.filter(aggregation_type_id=aggregation_type)

        equipment = Equipment.objects.prefetch_related(Prefetch(
            'aggregations', queryset=queryset))

        if not names:
            return equipment.all()

        return equipment.filter(name__in=names)
