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
            name="Who Doesn't Want Slippers",
            description="Thanks to an unlucky government mishap, the Department of Defense accidentally drafted a purchase order for 9 million pairs of slippers. However, their mistake can be your reward! The US Government is offering to send you your very own pair of slippers absolutely FREE!",
			instructions="Fill out the form below for a chance to recieve your pair of slippers.",
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
            formID = 'NameEmailPhoneNumberDog'
        )
        Campaign.objects.create(
            name="Help Me I Have ID10-T!",
            description="Does your computer shut down for seemingly no reason? Do pesky taskbars fill up your internet browser with ads and pop-ups? This is exceedingly common and stems from a rare disease called ID10-T. Literally millions of computer users are plagued with this debilitating ailment annually. Treatment is a free and easy application of C.O.M.M.O.N S.E.N.S.E.",
            instructions="Apply for your free ID10-T consultation today.",
            start_date=date(2015, 3, 1),
            end_date=date(2015, 5, 29),
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
except django.db.utils.OperationalError: 
    pass