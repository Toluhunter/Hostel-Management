from rest_framework import serializers

from .models import Report, Room, Category


class FetchReportSerialier(serializers.ModelSerializer):

    room = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Report
        exclude = ["description", "reported"]


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        exclude = ['reported']
        read_only_fields = ["id", "date_added", "resolved"]

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        if instance and "data" not in kwargs:
            self.fields["category"] = serializers.StringRelatedField()

    def validate(self, attrs):
        user = self.context["request"].user
        attrs["reported"] = user
        category = attrs["category"]
        category.amount_issues += 1
        category.save()
        return attrs


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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, attrs):
        if attrs["start_price"] > attrs["last_price"]:
            raise serializers.ValidationError(
                "Start Price Cannot be Higher than Last price")

        return attrs


class FetchCompileCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name", "start_price", "last_price"]


class FetchCompileSerilizer(serializers.ModelSerializer):

    room = serializers.StringRelatedField()
    category = FetchCompileCategorySerializer(read_only=True)

    class Meta:
        model = Report
        exclude = ["description", "reported"]


class DeleteReportSerilizer(serializers.Serializer):
    id = serializers.ListField()

    def validate(self, attrs):
        queryset = Report.objects.filter(id__in=attrs["id"])

        if len(queryset) != len(attrs["id"]):
            raise serializers.ValidationError({"id": "An Id in the list does not exist"})

        queryset.delete()

        return attrs


class ToggleReportSerializer(serializers.Serializer):

    id = serializers.ListField()

    def validate(self, attrs):

        queryset = Report.objects.filter(id__in=attrs["id"])

        if len(queryset) != len(attrs["id"]):
            raise serializers.ValidationError({"id": "An Id in the list does not exist"})

        for report in queryset:
            report.resolved = not report.resolved

            report.save()

        return attrs
