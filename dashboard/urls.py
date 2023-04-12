from django.urls import path
from . import views

urlpatterns = [
    path("issues/", views.FetchAmountReport.as_view(), name="amount-issues"),
    path("issues-per-year/", views.FetchIssueRatioMonth.as_view(), name="issues-per-year")
]
