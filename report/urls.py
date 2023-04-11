from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.CreateReportView.as_view(), name="add-report"),
    path("fetch-rooms/", views.FetchRoomsView.as_view(), name="fetch-rooms"),
    path("manage/<uuid:id>/", views.ManageReportView.as_view(), name="manage-reports"),
    path("toggle-resolve/<uuid:id>/", views.ToggleReportView.as_view(), name="toggle-report"),
    path("fetch-compile/", views.ListCompileView.as_view(), name="fetch-compile"),
    path("add-category/", views.CreateCategoryView.as_view(), name="add-category"),
    path("categories/", views.ListCategoryView.as_view(), name="categories"),
    path("", views.FetchReportView.as_view(), name="list-reports"),
]
