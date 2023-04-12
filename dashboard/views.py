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
