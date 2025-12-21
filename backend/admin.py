from django.contrib import admin
from .models import Room, Equipment, Booking

# Register your models here.
admin.site.register(Room)
admin.site.register(Equipment)
admin.site.register(Booking)