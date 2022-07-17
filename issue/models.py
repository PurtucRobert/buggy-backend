from django.db import models
from django.contrib.auth.models import User


class Detail(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    previous_status = models.CharField(max_length=255, blank=False, default='N')
    file = models.FileField(upload_to="issue/", blank=True)
    status = models.CharField(max_length=255, blank=False, default='N')


class Issue(models.Model):
    STATUS = [
        ('N', 'New'),
        ('A', 'Assigned'),
        ('V', 'Verified'),
        ('C', 'Closed'),
        ('H', 'On hold'),
    ]
    title = models.CharField(max_length=255, blank=False)
    status = models.CharField(
        max_length=1, default='N', blank=False, choices=STATUS
    )
    owner = models.ForeignKey(
        User, related_name='owned_issues', on_delete=models.DO_NOTHING
    )
    details = models.ManyToManyField(Detail)
