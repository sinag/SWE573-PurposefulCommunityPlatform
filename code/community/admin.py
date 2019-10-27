from django.contrib import admin
from .models import Community


class CommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'post_count']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'created_on', 'post_count')
    list_filter = ['created_on']
    search_fields = ['name']
    readonly_fields = ['created_on']


admin.site.register(Community, CommunityAdmin)
