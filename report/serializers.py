from rest_framework import serializers

from .models import Report, Room


class FetchReportSerialier(serializers.ModelSerializer):

    room = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Report
        exclude = ["description"]


class ReportSerializer(serializers.ModelSerializer):

    def get_category(self, obj):
        for cat_value, cat_name in obj.categories:
            if cat_value == obj.category:
                return cat_name
        return None

    class Meta:
        model = Report
        read_only_fields = ["id", "date_added", "resolved"]

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        if instance and "data" not in kwargs:
            self.fields["category"] = serializers.SerializerMethodField()


class DetailReportSerializer(serializers.ModelSerializer):

    room = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Report
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
