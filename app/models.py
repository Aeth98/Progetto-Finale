from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Item(models.Model):
    item = models.CharField(max_length=32)
    datetime = models.DateTimeField(auto_now_add=True)
    last_offer_usd = models.FloatField(null=True)
    last_offer_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    expire_date = models.DateTimeField()
    status = models.CharField(max_length=32, default='open')

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)



