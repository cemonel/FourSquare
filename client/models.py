from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):

	location = models.CharField(max_length=40, )
	venue = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return '%s  %s' % (self.location, self.venue)


class Favorite(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
	venue_id = models.CharField(max_length=50)
