from django.db import models


class Search(models.Model):

	location = models.CharField(max_length=40)
	venue = models.CharField(max_length=30)

	def __str__(self):
		return '%s  %s' % (self.location, self.venue)
