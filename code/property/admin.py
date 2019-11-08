from django.contrib import admin

from property.models import Property


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type', 'datatype']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'created_on', 'type', 'datatype')
    list_filter = ['datatype', 'type']
    search_fields = ['name', 'type', 'datatype']
    readonly_fields = ['created_on']


admin.site.register(Property, PropertyAdmin)
