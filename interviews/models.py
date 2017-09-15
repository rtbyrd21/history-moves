from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Images(models.Model):
	title = models.CharField(max_length=200)


class Themes(models.Model):
    theme = models.CharField(max_length=200)
    def __unicode__(self):
        return self.theme

    class Meta:
        ordering = ["theme"]
        verbose_name_plural = "themes"

class PlaceCategory(models.Model):
    type = models.CharField(max_length=128)
    def __unicode__(self):
        return self.type


class Excerpt(models.Model):
    extract = models.CharField(max_length=2000)
    beginning_time = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    themes = models.ManyToManyField(Themes, blank=True)
    images = models.ManyToManyField(Images, blank=True)
    def __unicode__(self):
		return self.extract

    class Meta:
        ordering = ["extract"]



class Women(models.Model):
    name = models.CharField(max_length=100)
    excerpt = models.ManyToManyField(Excerpt, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "women"

    def __unicode__(self):
		return self.name
    