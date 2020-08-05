from core.views import handle_exception_my, HandleExceptionMy
from rest_framework.viewsets import ViewSet, ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProductSets
from .serializers import MarketModelSerializer


class MarketViewSet(ModelViewSet):
    queryset = ProductSets.objects.all()
    serializer_class = MarketModelSerializer
