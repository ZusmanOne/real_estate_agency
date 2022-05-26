from django.contrib import admin

from .models import Flat,Complaint


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'owner_pure_phone')
    list_editable = ('new_building',)
    search_fields = ('town', 'town_district','address')
    readonly_fields = ('created_at',)
    list_filter = ('new_building',)
    raw_id_fields = ('like',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat_complaint')


admin.site.register(Flat, FlatAdmin,)
admin.site.register(Complaint, ComplaintAdmin)