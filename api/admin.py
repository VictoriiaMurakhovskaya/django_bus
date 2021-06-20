from django.contrib import admin
from .models import Station, Interval, Carrier, Carriage, Route

admin.site.register(Station)
admin.site.register(Interval)
admin.site.register(Carrier)
admin.site.register(Carriage)
admin.site.register(Route)
