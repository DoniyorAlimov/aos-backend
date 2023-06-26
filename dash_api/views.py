from rest_framework.viewsets import ModelViewSet
from .models import Aggregation
from .serializers import AggregationSerializer


class AggregationViewSet(ModelViewSet):
    http_method_names = ['get']

    queryset = Aggregation.objects.select_related(
        'equipment').select_related('aggregation_type').all()
    serializer_class = AggregationSerializer
