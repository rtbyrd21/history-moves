from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Images(models.Model):
	title = models.CharField(max_length=200)

class Themes(models.Model):
    theme = models.CharField(max_length=200)
    def __unicode__(self):
        return self.theme

class RelatedStages(models.Model):
    stage = models.CharField(max_length=200)
    def __unicode__(self):
        return self.stage

class RelatedPeople(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class RelatedYears(models.Model):
    year = models.CharField(max_length=11)
    def __unicode__(self):
        return self.year

class RelatedThings(models.Model):
    thing = models.CharField(max_length=200)
    def __unicode__(self):
        return self.thing

class PlaceCategory(models.Model):
    type = models.CharField(max_length=128)
    def __unicode__(self):
        return self.type

class Neighborhoods(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class MapFeatures(models.Model):
    feature = models.CharField(max_length=128)
    def __unicode__(self):
        return self.feature

class Address(models.Model):
    address_1 = models.CharField(_("address"), max_length=128, null=True, blank=True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, null=True, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Brooklyn")
    state = models.CharField(_("state"), default="NY", max_length=2)
    zip_code = models.CharField(_("zip code"), max_length=5, default="112", null=True, blank=True)
    def __unicode__(self):
        return self.address_1


class Location(models.Model):
    name = models.CharField(max_length=200)
    neighborhood = models.ManyToManyField(Neighborhoods, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    place_category = models.ForeignKey(PlaceCategory, null=True, blank=True)
    map_features = models.ManyToManyField(MapFeatures, blank=True)
    images = models.ManyToManyField(Images, blank=True)
    def __unicode__(self):
		return unicode(self.name)

class Event(models.Model):
    extract = models.CharField(max_length=201)
    beginning_time = models.IntegerField(null=True, blank=True)
    location = models.ManyToManyField(Location, blank=True)
    stage = models.ManyToManyField(RelatedStages, blank=True)
    themes = models.ManyToManyField(Themes, blank=True)
    years = models.ManyToManyField(RelatedYears, blank=True)
    people = models.ManyToManyField(RelatedPeople, blank=True)
    things = models.ManyToManyField(RelatedThings, blank=True)
    images = models.ManyToManyField(Images, blank=True)
    def __unicode__(self):
		return self.extract


class Person(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, null=True, blank=True)
    event = models.ManyToManyField(Event, blank=True)

    def __unicode__(self):
		return self.name
    