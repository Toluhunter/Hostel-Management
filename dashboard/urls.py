from django.urls import path
from . import views

urlpatterns = [
    path("issues/", views.FetchAmountReport.as_view(), name="amount-issues")
]
