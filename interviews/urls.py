from django.conf.urls import url, include

from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'women', views.WomenViewSet)
router.register(r'excerpts', views.ExcerptViewSet)
router.register(r'themes', views.ThemeViewSet)
router.register(r'images', views.RelatedImagesViewSet)
# router.register(r'related-themes', views.RelatedThemeViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]