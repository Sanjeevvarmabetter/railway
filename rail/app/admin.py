from django.contrib import admin
from .models import Train, Station, Ticket

admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Ticket)
