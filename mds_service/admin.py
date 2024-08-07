from django.contrib import admin

from mds_service.models import Direction, Doctor, Service, Appointment


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name_direction", "description")
    list_editable = ("name_direction", "description")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "photo", "direction")
    search_fields = ["last_name"]
    list_editable = ("first_name", "last_name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name_service", "description", "direction", "price")
    list_editable = ("name_service", "direction", "price")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "service", "doctor", "date")
    list_editable = ("user", "service", "doctor", "date")
