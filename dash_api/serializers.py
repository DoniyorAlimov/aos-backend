from rest_framework import serializers
from .models import Aggreagation_Type, Aggregation, Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name']


class AggregationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggreagation_Type
        fields = ['id', 'name', 'unit']


class AggregationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregation
        fields = ['id', 'equipment', 'value',
                  'timestamp', 'aggregation_type']

    equipment = EquipmentSerializer()
    aggregation_type = AggregationTypeSerializer()
