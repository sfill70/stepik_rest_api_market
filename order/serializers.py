from rest_framework.serializers import Serializer, ModelSerializer, CharField
from rest_framework import serializers
from .models import Order
from logging import getLogger

_logger = getLogger(__name__)


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        # _logger.warning(validated_data)
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # _logger.warning(validated_data)
        # Поля допущенные к изменению
        instance.delivery_address = validated_data.get('delivery_address', instance.delivery_address)
        # "created" оставим если всетаки передумает
        if validated_data['status'] == "created" or validated_data['status'] == 'cancelled':
            instance.status = validated_data.get('status', instance.status)
        # Поля не допущенные к изменению ну в принципе все остальные
        # instance.recipient = validated_data.get('recipient', instance.recipient, )
        # instance.product_set = validated_data.get('product_set', instance.product_set)
        instance.save()
        return instance
