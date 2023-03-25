from rest_framework import serializers

from .models import Report


class FetchReportSerialier(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude = ["description", "category"]


class CreateReportSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Report
        exclude = ["date_added", "status"]


class DetailReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        exclude = ["category"]
