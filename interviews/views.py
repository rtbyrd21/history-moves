from django.shortcuts import render

from django.http import HttpResponse
import django_filters
from rest_framework import viewsets
from serializers import *


class RelatedImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = RelatedImagesSerializer

# class RelatedWomenViewSet(viewsets.ModelViewSet):
#     queryset = RelatedWomen.objects.all()
#     serializer_class = RelatedWomenSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all()
    serializer_class = ThemeSerializer


class ExcerptViewSet(viewsets.ModelViewSet):
    queryset = Excerpt.objects.all()
    serializer_class = ExcerptSerializer



class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = RelatedWomenSerializer

# class RelatedThemeViewSet(viewsets.ModelViewSet):
#     queryset = Themes.objects.all()
#     serializer_class = RelatedThemeSerializer


