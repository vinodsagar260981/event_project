from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=150)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=10)
    phone = models.CharField('Contact Number',max_length=15)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email')

    def __str__(self):
        return self.name

class EventUser(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=150)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    attendees = models.ManyToManyField(EventUser, blank=True)

    def __str__(self):
        return self.name