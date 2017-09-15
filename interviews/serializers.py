from rest_framework import serializers
from models import *

class RelatedImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ("title",)



class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 3
        model = Themes
        fields = ("theme", "excerpt_set",)


class ExcerptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Excerpt
        # women = RelatedWomenSerializer
        images = RelatedImagesSerializer
        fields = ('extract', 'beginning_time', 'themes', 'images', 'women_set')

class RelatedWomenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Women
        excerpt = ExcerptSerializer
        fields = ("name","excerpt")


