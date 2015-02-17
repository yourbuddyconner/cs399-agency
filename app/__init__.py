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
		Campaign.objects.create(
			name = "SickNasty Air Guitar",
			description = "Have you always wished that you could play the guitar, but never had the time or motivation to learn? Well, a new innovation from Hasbruh&reg; lets anyone do just that! Just wave your hands in front of the guitar modoule and let the SickNasty Air Guitar take care of the music.",
			instructions = "Fill out the form below and get a free Air Guitar!",
			start_date = date(2015, 6, 1),
			end_date = date(2016, 6, 30)
		)
except django.db.utils.OperationalError: 
	pass