from django.db import models
from uuid import uuid4


class Room(models.Model):

    name = models.CharField(max_length=4, null=False, blank=False, unique=True)


class Report(models.Model):

    categories = [
        (1, "Electrical"),
        (2, "Carpentry"),
        (3, "Plumbing"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4)
    issue = models.CharField(max_length=25, null=False, blank=False)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    category = models.IntegerField(choices=categories, null=False, blank=False)
    resolved = models.BooleanField(default=False, null=False, blank=False)
    snapshot = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("issue", "room")

    @property
    def get_category(self):
        for cat_value, cat_name in self.categories:
            if cat_value == self.category:
                return cat_name
        return None

    def __str__(self):
        return f"{self.room} {self.title}"
