from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import requests
from requests.exceptions import Timeout
from .util_recipient import recipients_url, list_recipient_json
from core.views import handle_exception_my
from .models import Recipient
from .serializers import RecipientModelSerializer


# @handle_exception_my
# @api_view(http_method_names=['GET'])
# def recipients(request: Request) -> Response:
#     try:
#         recipients_req = requests.get(recipients_url, timeout=10)
#         if recipients_req.status_code == 404:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         recipients_list = recipients_req.json()
#         recipients_list = list_recipient_json(recipients_list)
#     except Timeout:
#         return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
#     if recipients_list:
#         return Response(recipients_list)

@handle_exception_my
@api_view(http_method_names=['GET', 'POST'])
def recipients(request: Request) -> Response:
    if request.method == 'GET':
        books = Recipient.objects.all()
        serializer = RecipientModelSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecipientModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @handle_exception_my
# @api_view(http_method_names=['GET'])
# def recipient_detail(request: Request, pk: int) -> Response:
#     try:
#         recipients_req = requests.get(recipients_url, timeout=10)
#         if recipients_req.status_code == 404:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         recipients_list = recipients_req.json()
#         recipients_list = list_recipient_json(recipients_list)
#     except Timeout:
#         return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
#     response = None
#     for index, recipient in enumerate(recipients_list):
#         if index == pk:
#             response = recipient
#     if response:
#         return Response(response)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

@handle_exception_my
@api_view(http_method_names=['GET','PUT'])
def recipient_detail(request: Request, pk: int) -> Response:
    def get_object(pk):
        try:
            return Recipient.objects.get(pk=pk)
        except Recipient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        recipient = get_object(pk)
        serializer = RecipientModelSerializer(recipient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        recipient = get_object(pk)
        print(recipient)
        serializer = RecipientModelSerializer(recipient, data=request.data)
        print(serializer)
        if serializer.is_valid():
            print("_____________________________________")
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
