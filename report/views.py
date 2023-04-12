from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Report, Room, Category
from .permissions import IsReporter
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
    permission_classes = [IsAuthenticated, IsReporter]
    parser_classes = [MultiPartParser]

    def get_object(self):
        id = self.kwargs["id"]
        obj = get_object_or_404(Report, id=id)
        self.check_object_permissions(self.request, obj)
        return obj


class ToggleReportView(generics.GenericAPIView):
    '''
    Toggle Whethere Issue Has Been Solved or not   
    '''

    serializer_class = serializers.ToggleReportSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"Success": True, "Message": "Toggle Successful"}, status=status.HTTP_200_OK)


class DeleteReportView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.DeleteReportSerilizer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"success": True, "message": "Deleted Successfully"})


class DeleteCategoryView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        id = self.kwargs["id"]
        obj = get_object_or_404(Category, id=id)
        return obj


class FetchRoomsView(generics.ListAPIView):

    serializer_class = serializers.RoomSerializer
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()


class CreateCategoryView(generics.CreateAPIView):

    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ListCategoryView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()


class ListCompileView(generics.ListAPIView):

    serializer_class = serializers.FetchCompileSerilizer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Report.objects.all()
