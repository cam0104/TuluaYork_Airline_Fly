from django.contrib import admin

from core.flight.models import *

admin.site.register(flight)
admin.site.register(airport)
admin.site.register(airline)
admin.site.register(requirement)
admin.site.register(booking)


