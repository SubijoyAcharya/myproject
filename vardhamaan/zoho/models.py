from django.db import models


class zoho(models.Model):
 name= models.CharField(max_length=255)
 price=models.FloatField()
 stock=models.IntegerField()
 imageurl=models.CharField(max_length=300)
