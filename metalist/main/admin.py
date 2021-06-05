from django.contrib import admin
from .models import Matches, Teams, Profile, Tickets


admin.site.register(Matches)
admin.site.register(Teams)
admin.site.register(Profile)
admin.site.register(Tickets)