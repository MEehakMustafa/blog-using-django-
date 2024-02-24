from django.db import models

# Create your models here.
class post(models.Model):
    from datetime import datetime
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100000)
    created_at=models.DateTimeField(default=datetime.now, blank=True)