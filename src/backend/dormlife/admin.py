from django.contrib import admin
from .models import Room, Resident, Announcement, Staff, Request

admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(Announcement)
admin.site.register(Staff)
admin.site.register(Request)