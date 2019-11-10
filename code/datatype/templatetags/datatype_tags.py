from django import template

from community.models import Community
from datatype.models import DataType

register = template.Library()


@register.filter
def community_name(community__id):
    return Community.objects.get(id=community__id).name


@register.filter
def community_id(datatype_id):
    return DataType.objects.get(id=datatype_id).community.id


@register.filter
def field_count(datatype_id):
    return DataType.objects.get(id=datatype_id).property_set.all().count()


@register.filter
def reference_count(datatype_id):  # Todo - add existing post control, inherited property control
    return DataType.objects.get(id=datatype_id).property_set.all().count()
