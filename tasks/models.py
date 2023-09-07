from django.db import models


# Create your models here.
class Tasks(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ["created_at"]
