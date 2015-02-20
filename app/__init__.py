from app.models import Campaign
from datetime import date
import django.db.utils

try: 
    if not Campaign.objects.all():
        Campaign.objects.create(
            name="Fruity Pebble Bites",
            description="A campaign for General Mills' new product, Fruity Pebbles Bites. It's the new, " +
                        "fun way to consume massive amounts of processed sugar and food dyes!",
            instructions="Fill out the form below and get a free case of fruity, sugary goodness!",
            start_date=date(2015, 1, 1),
            end_date=date(2016, 5, 29),
            formID = 'NameTwitterPhonenumberEmail'
        )
        Campaign.objects.create(
            name="SickNasty Air Guitar",
            description="Have you always wished that you could play the guitar, but never had the time or motivation " +
                        "to learn? Well, a new innovation from Hasbruh&reg; lets anyone do just that! Just wave your " +
                        "hands in front of the guitar modoule and let the SickNasty Air Guitar take care of the music.",
            instructions="Fill out the form below and get a free Air Guitar!",
            start_date=date(2015, 6, 1),
            end_date=date(2016, 6, 30),
            formID = 'TwitterEmail'
        )
        Campaign.objects.create(
            name="Who Doesn't Want Slippers",
            description="Once, long ago you",
			instructions="Fill out the form below for a chance to win a pair of glass slippers",
            start_date=date(2015, 2, 1),
            end_date=date(2016, 2, 20),
            formID = 'NameEmail'
        )
        Campaign.objects.create(
            name="Dog Fancy USA",
            description=" Having a ruff day? Where on earth would you go if you needed a well-trained pup to star in your commercial " +
                        "for organic dog chow? Right here, of course! At Dog Fancy USA, we make it our goal to find" +
                        "you the best mut for your cut.",
            instructions="Fill out the form below to win a free dog!",
            start_date=date(2015,2,1),
            end_date=date(2015,3,1),
            formID = 'FullnameAddressSocialSecurityShamefulHighSchoolEmailCurrentHumidyLevelFirstPetsNameChildsBirthdayAnyOtherPossibleThingThatICouldUseToStealYourIdentity'
        )
except django.db.utils.OperationalError: 
    pass