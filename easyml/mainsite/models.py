import django
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email

class CsvFile(models.Model):

    file_owner = models.ForeignKey(
        'CustomUser',
        related_name="file_owner",
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)

class CsvFileData(models.Model):

    parent_file = models.ForeignKey(
        'CsvFile',
        related_name="parent_file",
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    column_header = models.CharField(max_length=255)
    data = models.FloatField(null=True, blank=True)
    row_num = models.IntegerField(null=False, blank=False)
    column_num = models.IntegerField(null=False, blank=False)

