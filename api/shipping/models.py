from django.contrib.auth.models import AbstractUser
from django.db import models


# just following django convention
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


# could use uuid ,for the demo sake default id is just fine and efficient
class Package(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="p_sender"
    )
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="p_receiver"
    )
    weight = models.FloatField()
    STATUS = {"on": "On the way", "done": "Delivered !"}
    status = models.CharField(max_length=4, choices=STATUS, default="on")
    created = models.DateTimeField(auto_now_add=True)
    received_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def get_total_cost(self):
        return f"{self.weight * 5000.00} kyat"
