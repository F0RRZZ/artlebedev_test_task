from django.contrib import admin

from parks.models import Park


@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = (
        Park.name.field.name,
        Park.address.field.name,
        Park.organization.field.name,
        Park.website.field.name,
        Park.inn.field.name,
    )
