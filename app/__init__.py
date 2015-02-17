from app.models import Campaign
from datetime import date
import django.db.utils

try: 
	if not Campaign.objects.all():
		Campaign.objects.create(
			name = "Fruity Pebble Bites",
			description = "A campaign for General Mills' new product, Fruity Pebbles Bites. It's the new, fun way to consume massive amounts of processed sugar and food dyes! Fill out the form below to get your free sample case.",
			start_date = date(2015, 1, 1),
			end_date = date(2016, 5, 29)
		)
except django.db.utils.OperationalError: 
	pass