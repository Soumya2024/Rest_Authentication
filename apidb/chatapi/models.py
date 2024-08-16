from django.db import models
# Create your models here.


class MergedData(models.Model):
    json_data = models.JSONField()  # Use JSONField if you're using PostgreSQL, otherwise TextField
    created_at = models.DateTimeField(auto_now_add=True)
