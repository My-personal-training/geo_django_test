from django.contrib.gis import admin
from .models import Category, City, Place

# Register your models here.
admin.site.register(Category)

# Creating interface
class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 4,
            'default_lon': 133.74,
            'default_lat': -24.06
        }
    }

@admin.register(Place)
class PlaceAdmin(CustomGeoAdmin):
    pass

@admin.register(City)
class PlaceAdmin(CustomGeoAdmin):
    pass