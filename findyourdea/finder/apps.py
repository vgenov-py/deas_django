from django.apps import AppConfig
import geocoder

g = geocoder.ip("me")
print(g.latlng)

class FinderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finder'
