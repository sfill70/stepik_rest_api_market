from rest_framework.serializers import Serializer, ModelSerializer, CharField
from rest_framework import serializers
from .models import Recipient


class RecipientSerializer(Serializer):
    # """TODO"""
    surname = CharField(max_length=100, required=True)
    name = CharField(max_length=100, required=True)
    patronymic = CharField(max_length=100, required=True)
    phone_number = CharField(max_length=100, required=True)

    def create(self, validated_data):
        return Recipient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic, )
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


class RecipientModelSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'

    def create(self, validated_data):
        return Recipient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic, )
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance
