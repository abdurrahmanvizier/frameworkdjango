from django.shortcuts import render

from rest_framework.decorators import api_view, action, permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.views import APIView

from framework.models import Object

from restapi.serializers import ObjectSerializer
from restapi.filters import ObjectFilter
from restapi.permissions import IsOwner
# Create your views here.

@api_view(['GET'],)
def index(request):
    messages = "TESTING API HERE"
    return Response(data=messages, status=status.HTTP_200_OK)


class ObjectAll(APIView):

    def get_object(self):
        try:
            return Object.objects.all()
        except Object.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get(self, request, format=None):
        queryset = Object.objects.all()
        serializer = ObjectSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    
    filterset_class = ObjectFilter

    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwner
    )

    @action(methods=['GET'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('sourcesystemcreatedtime').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
            
        