from django.db import models

# Create your models here.


class FlagHalfMastInfo(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255)

