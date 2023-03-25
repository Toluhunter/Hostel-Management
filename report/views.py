from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers


class CreateReportView(generics.CreateAPIView):
    serializer_class = serializers.CreateReportSerializer
    permission_classes = [IsAuthenticated]


class FetchReportView(generics.ListAPIView):
    serializer_class = serializers.FetchReportSerialier
    permission_classes = [IsAuthenticated]
