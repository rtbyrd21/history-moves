from rest_framework import serializers
from models import *

class RelatedImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ("title",)

class RelatedThingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelatedThings
        fields = ("thing",)

class RelatedPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelatedPeople
        fields = ("name",)

class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelatedYears
        fields = ("year",)

class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Themes
        fields = ("theme",)

class StageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelatedStages
        fields = ("stage",)


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ("address_1", "address_2", "city", "state", "zip_code",)


class PlaceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = ("type",)

class MapFeaturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapFeatures
        fields = ("feature",)

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Location
        address = AddressSerializer
        place_category = PlaceCategorySerializer
        map_features = MapFeaturesSerializer
        images = RelatedImagesSerializer
        fields = ("name", "neighborhood", "address", "latitude", "longitude", "place_category", "map_features", "images",)



class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Event
        location = LocationSerializer
        stage = StageSerializer
        theme = ThemeSerializer
        years = YearSerializer
        people = RelatedPeopleSerializer
        thing = RelatedThingsSerializer
        images = RelatedImagesSerializer
        fields = ('extract', 'beginning_time', 'location', 'stage', 'themes', 'years', 'people', 'things', 'images',)

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Person
        event = EventSerializer
        fields = ("name","color","event")

