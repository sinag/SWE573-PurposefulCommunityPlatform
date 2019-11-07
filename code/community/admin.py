from django.contrib import admin
from .models import Community, DataType, Property, Instance, TextField, IntegerField


class CommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'post_count', 'author']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'created_on', 'post_count', 'author')
    list_filter = ['author']
    search_fields = ['name', 'author']
    readonly_fields = ['created_on']


class TextFieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'property', 'value']}),
    ]
    list_display = ('id', 'instance', 'property', 'value')
    list_filter = ['instance', 'property']
    search_fields = ['instance', 'property']


class IntegerFieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'property', 'value']}),
    ]
    list_display = ('id', 'instance', 'property', 'value')
    list_filter = ['instance', 'property']
    search_fields = ['instance', 'property']


class DataTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'author', 'generic']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'created_on', 'author', 'generic')
    list_filter = ['author', 'generic']
    search_fields = ['name', 'author', 'generic']
    readonly_fields = ['created_on']


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type', 'datatype']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'created_on', 'type', 'datatype')
    list_filter = ['datatype', 'type']
    search_fields = ['name', 'type', 'datatype']
    readonly_fields = ['created_on']


class InstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['author', 'datatype']}),
        ('Date information', {'fields': ['created_on', 'updated_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'author', 'created_on', 'updated_on', 'datatype')
    list_filter = ['datatype', 'author']
    search_fields = ['datatype', 'author']
    readonly_fields = ['created_on', 'updated_on']


admin.site.register(TextField, TextFieldAdmin)
admin.site.register(IntegerField, IntegerFieldAdmin)
admin.site.register(Instance, InstanceAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(DataType, DataTypeAdmin)
