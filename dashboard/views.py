from datetime import datetime
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from report.models import Report


class FetchAmountReport(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        record = {}
        record["resolved"] = Report.objects.filter(resolved=True).count()
        record["unresolved"] = Report.objects.filter(resolved=False).count()

        return Response(record)


class FetchIssueRatioMonth(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):

        record = {
            "Jan": 0,
            "Feb": 0,
            "Mar": 0,
            "Apr": 0,
            "May": 0,
            "Jun": 0,
            "Jul": 0,
            "Aug": 0,
            "Sep": 0,
            "Oct": 0,
            "Nov": 0,
            "Dec": 0
        }

        year = datetime.now().year
        for month, num in zip(record.keys(), range(1, 13)):
            record[month] = Report.objects.filter(
                date_added__month=num, date_added__year=year).count()

        return Response(record)
