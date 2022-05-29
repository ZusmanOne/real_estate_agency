from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    search_fields = ('town', 'town_district', 'address')
    readonly_fields = ('created_at',)
    list_filter = ('new_building',)
    raw_id_fields = ('likes',)
    inlines = [
        OwnerInline
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('owner',)
    raw_id_fields = ('flat',)



