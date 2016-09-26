from django.shortcuts import render

from django.http import HttpResponse
import django_filters
from rest_framework import viewsets
from serializers import *



class MapFeaturesViewSet(viewsets.ModelViewSet):
    queryset = MapFeatures.objects.all()
    serializer_class = MapFeaturesSerializer

class PlaceCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlaceCategory.objects.all()
    serializer_class = PlaceCategorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = PlaceCategory.objects.all()
        place = self.request.query_params.get('place', None)
        if place is not None:
            queryset = queryset.filter(type=place)
        return queryset

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class RelatedImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = RelatedImagesSerializer

class RelatedThingsViewSet(viewsets.ModelViewSet):
    queryset = RelatedThings.objects.all()
    serializer_class = RelatedThingsSerializer

class RelatedPeopleViewSet(viewsets.ModelViewSet):
    queryset = RelatedPeople.objects.all()
    serializer_class = RelatedPeopleSerializer

class YearViewSet(viewsets.ModelViewSet):
    queryset = RelatedYears.objects.all()
    serializer_class = YearSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all()
    serializer_class = ThemeSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = RelatedStages.objects.all()
    serializer_class = StageSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PeopleSerializer


