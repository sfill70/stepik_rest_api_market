from rest_framework.serializers import ModelSerializer
from .models import ProductSets


class MarketModelSerializer(ModelSerializer):
    class Meta:
        model = ProductSets
        fields = '__all__'

    def create(self, validated_data):
        return ProductSets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
