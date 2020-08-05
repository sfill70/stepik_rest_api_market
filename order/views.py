from django.db.models import QuerySet, Q
from django.shortcuts import render
from logging import getLogger
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.response import Response
from core.views import HandleExceptionMy
from .models import Order
from .serializers import OrderModelSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSet, ModelViewSet
from datetime import datetime, date, time

_logger = getLogger(__name__)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    # _logger.warning(queryset)
    serializer_class = OrderModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_created_datetime', 'product_set']

    # Экшен для фильтрации по конкретной дате, в стандартном варианте, унжно вводить до секунды
    @action(detail=False, methods=['get'])
    def filter_order(self, request):
        if request.query_params:
            data_order = request.query_params.get('data_order', None)
            data_obj = datetime.strptime(data_order, '%Y-%m-%d').date()
            # _logger.warning(data_obj)
            queryset = Order.objects.all()
            # Это  работает
            result = Order.objects.filter(Q(order_created_datetime__date=data_obj))
            # Это не работает
            # result = Order.objects.filter(order_created_datetime__gt=data_obj)
            # Это  работает
            # result = {i for i in queryset if i.order_created_datetime.date() == data_obj}
            if data_order:
                # _logger.warning(data_order)
                serializer = OrderModelSerializer(result, many=True)
                return Response(serializer.data)
        else:
            return Response({'message': 'Нужны данные /?data_order=%Y-%m-%d'})
