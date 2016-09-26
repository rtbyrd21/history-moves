from django.conf.urls import url, include

from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'people', views.PeopleViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'stages', views.StageViewSet)
router.register(r'themes', views.ThemeViewSet)
router.register(r'years', views.YearViewSet)
router.register(r'related-people', views.RelatedPeopleViewSet)
router.register(r'related-things', views.RelatedThingsViewSet)
router.register(r'images', views.RelatedImagesViewSet)
router.register(r'map-features', views.MapFeaturesViewSet)
router.register(r'place-category', views.PlaceCategoryViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]