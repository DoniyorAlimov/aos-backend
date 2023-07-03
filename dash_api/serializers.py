from rest_framework import serializers
from .models import Aggreagation_Type, Aggregation, Equipment


class SimpleEquipmentSerializer(serializers.ModelSerializer):
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

    equipment = SimpleEquipmentSerializer()
    aggregation_type = AggregationTypeSerializer()


class SimpleAggregationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregation
        fields = ['id', 'value', 'timestamp', 'aggregation_type']

    aggregation_type = AggregationTypeSerializer()


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'aggregations']

    aggregations = SimpleAggregationSerializer(many=True)


class SimpleEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name']
