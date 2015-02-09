from django.db import models
from django.utils import timezone

class Campaign(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	start_date = models.DateField('day the campaign begins')
	end_date = models.DateField('day the campaign ends')

	# returns a friendly name for django
	def __unicode__(self):
		return self.name