from rest_framework.serializers import Serializer, ModelSerializer, CharField
from rest_framework import serializers
from .models import Recipient
from logging import getLogger

_logger = getLogger(__name__)


class RecipientSerializer(Serializer):
    surname = CharField(max_length=100, required=True)
    name = CharField(max_length=100, required=True)
    patronymic = CharField(max_length=100, required=True)
    phone_number = CharField(max_length=100, required=True)

    def create(self, validated_data):
        return Recipient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # _logger.warning(validated_data)
        # _logger.warning('&&&&&&&&&&&&&&&&&&&')
        instance.surname = validated_data.get('surname', instance.surname)
        instance.save()
        return instance


class RecipientModelSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'

    def create(self, validated_data):
        # _logger.warning(validated_data)
        return Recipient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # _logger.warning(validated_data)
        # Поля допущенные к изменению
        instance.name = validated_data.get('name', instance.name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic, )
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


class RecipientModelSerializer2(RecipientModelSerializer):
    def update(self, instance, validated_data):
        # _logger.warning(validated_data)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.save()
        return instance
