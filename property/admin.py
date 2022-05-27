from django.contrib import admin

from .models import Flat,Complaint,Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owner_flat.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'price', 'new_building', 'construction_year', 'owner_pure_phone')
    list_editable = ('new_building',)
    search_fields = ('town', 'town_district','address')
    readonly_fields = ('created_at',)
    list_filter = ('new_building',)
    raw_id_fields = ('like',)
    inlines = [
        OwnerInline
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat_complaint')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('owner',)
    raw_id_fields = ('owner_flat',)


admin.site.register(Flat, FlatAdmin,)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
