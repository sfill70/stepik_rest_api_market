from logging import getLogger
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import requests
from core.views import handle_exception_my
from .models import Recipient
from .serializers import RecipientModelSerializer, RecipientSerializer, RecipientModelSerializer2
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSet, ModelViewSet

_logger = getLogger(__name__)


# __all__ = [
#

class RecipientsViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    # _logger.warning(queryset)
    serializer_class = RecipientModelSerializer


    @action(detail=True, methods=['patch'])
    def change_surname(self, request, pk=None):
        instance = self.get_object()
        # _logger.warning(request.data)
        serializer = RecipientModelSerializer2(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
