from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)