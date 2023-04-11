from uuid import uuid4

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


Account = get_user_model()


class Room(models.Model):

    name = models.CharField(max_length=4, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(unique=True, null=False, max_length=30)
    start_price = models.IntegerField(validators=[MinValueValidator(
        500), MaxValueValidator(10_000)], null=False, blank=False)
    last_price = models.IntegerField(
        validators=[MaxValueValidator(40_000)], null=False, blank=False)

    def __str__(self):
        return self.name


class Report(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    issue = models.CharField(max_length=25, null=False, blank=False)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="report")
    reported = models.ForeignKey(
        to=Account, null=True, on_delete=models.SET_NULL, default=None)
    resolved = models.BooleanField(default=False, null=False, blank=False)
    snapshot = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("issue", "room")

    def __str__(self):
        return f"{self.room} {self.issue}"
