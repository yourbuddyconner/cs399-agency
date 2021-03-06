from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.forms import ModelForm
import datetime


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    start_date = models.DateField('day the campaign begins')
    end_date = models.DateField('day the campaign ends')
    formID = models.CharField(max_length=100, default='')

    def isRunning(self):
        today = datetime.date.today()
        return self.start_date < today and today < self.end_date

    # returns a friendly name for django
    def __unicode__(self):
        return self.name


# use this model for the campaign forms
class InterestedUser(models.Model):
    # Name
    name = models.CharField(max_length=100)
    # Other Fields
    twitter_regex = RegexValidator(regex=r'@([A-Za-z0-9_]+)',
                                 message="Please enter a valid twitter handle.")
    twitter_handle = models.CharField(validators=[twitter_regex], max_length=100, null=True)
    # Phone Number
    # taken from http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'." +
                                         " Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20)  # validators should be a list

    dog_preferance = models.CharField(max_length = 100, null=True)
    # E-Mail Address
    email = models.EmailField(max_length=254)
    def __unicode__(self):
        return self.name


# example form model
class NameTwitterPhonenumberEmail(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['name', 'twitter_handle', 'phone_number', 'email']

class NamePhonenumberEmail(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['name', 'phone_number', 'email']

class NameEmail(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['name', 'email']

class TwitterPhonenumberEmail(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['twitter_handle', 'phone_number', 'email']

class TwitterPhonenumber(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['twitter_handle', 'phone_number']

class TwitterEmail(ModelForm):
    class Meta:
        model = InterestedUser
        fields = [ 'twitter_handle', 'email']

class Email(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['email']

class NameEmailPhoneNumberDog(ModelForm):
    class Meta:
        model = InterestedUser
        fields = ['name', 'email', 'phone_number', 'dog_preferance']
