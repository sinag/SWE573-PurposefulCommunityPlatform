from django.contrib import admin

from property.models import Property


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type', 'datatype', 'author']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'type', 'datatype', 'author')
    list_filter = ['author', 'datatype', 'type']
    search_fields = ['name', 'datatype', 'author', 'type']
    readonly_fields = ['created_on']


admin.site.register(Property, PropertyAdmin)
