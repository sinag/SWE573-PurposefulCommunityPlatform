from django.contrib import admin
from .models import Community


class CommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'post_count', 'author']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'created_on', 'post_count', 'author')
    list_filter = ['author']
    search_fields = ['name', 'author']
    readonly_fields = ['created_on']


admin.site.register(Community, CommunityAdmin)
