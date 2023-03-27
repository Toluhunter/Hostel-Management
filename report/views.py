from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Report, Room
from . import serializers


class CreateReportView(generics.CreateAPIView):
    serializer_class = serializers.ReportSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]


class FetchReportView(generics.ListAPIView):
    serializer_class = serializers.FetchReportSerialier
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()


class ManageReportView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ReportSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self):
        id = self.kwargs["id"]
        obj = get_object_or_404(Report, id=id)
        self.check_object_permissions(self.request, obj)
        return obj


class FetchRoomsView(generics.ListAPIView):

    serializer_class = serializers.RoomSerializer
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
