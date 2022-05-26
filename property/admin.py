from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'owner')
    search_fields = ('town', 'town_district','address')


admin.site.register(Flat, FlatAdmin,)
