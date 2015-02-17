from app.models import Campaign
from datetime import date
import django.db.utils

try: 
	if not Campaign.objects.all():
		Campaign.objects.create(
			name = "Fruity Pebble Bites",
			description = "A campaign for General Mills' new product, Fruity Pebbles Bites. It's the new, fun way to consume massive amounts of processed sugar and food dyes!",
			instructions = "Fill out the form below and get a free case of fruity, sugary goodness!",
			start_date = date(2015, 1, 1),
			end_date = date(2016, 5, 29)
		)
except django.db.utils.OperationalError: 
	pass