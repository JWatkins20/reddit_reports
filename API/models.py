from django.db import models

class ticker_mentions(models.Model):
	name = models.CharField(max_length=5)
	time = models.DateTimeField()
	mentions = models.IntegerField()

class ticker_details(models.Model):
	company = models.CharField(max_length=50)
	ticker_name = models.CharField(max_length=5)