from django.contrib import admin

from .models import *

# Register your models here.
class Flightadmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    
    
class Passengeradmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    list_display = ("first", "last")
    
    
class Airportadmin(admin.ModelAdmin):
    list_display = ("city", "code")

admin.site.register(Flight, Flightadmin)
admin.site.register(Airport, Airportadmin)
admin.site.register(Passenger, Passengeradmin)



