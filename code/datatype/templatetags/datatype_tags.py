from django import template

from community.models import Community
from datatype.models import DataType
from datetimefield.models import DateTimeField
from instance.models import Instance
from integerfield.models import IntegerField
from textfield.models import TextField

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
def reference_count(datatype_id):
    return Instance.objects.filter(datatype_id=datatype_id).count()


@register.filter
def post_count(datatype_id):
    return Instance.objects.filter(datatype_id=datatype_id).count()


@register.simple_tag
def datatype_fields(datatype_id):
    return DataType.objects.get(id=datatype_id).fields


# Todo - this tag also exists in community_tags, think about merge
@register.filter
def field_type_to_input_type(field_type):
    result = "text"
    if field_type == 0:
        result = "text"
    if field_type == 1:
        result = "number"
    if field_type == 2:
        result = "datetime-local"
    if field_type == 4:
        result = "url"
    if field_type == 5:
        result = "url"
    if field_type == 6:
        result = "image"
    if field_type == 7:
        result = "email"
    if field_type == 8:
        result = "url"
    return result


@register.filter
def datatype_name(datatype_id):
    return DataType.objects.get(id=datatype_id).name


@register.simple_tag
def property_value(instance_id, property_id, property_type):
    if property_type == 0 or property_type == 4 or property_type == 5 or property_type == 6 or property_type == 7 or property_type == 8:
        result = TextField.objects.filter(instance_id=instance_id).filter(property_id=property_id).first()
        if result is not None:
            return result.value
        else:
            return ''
    if property_type == 1:
        result = IntegerField.objects.filter(instance_id=instance_id).filter(property_id=property_id).first()
        if result is not None:
            if result.value is not None:
                return result.value
            else:
                return ''
        else:
            return ''
    if property_type == 2:
        result = DateTimeField.objects.filter(instance_id=instance_id).filter(property_id=property_id).first()
        if result is not None:
            if result.value is not None:
                return result.value.strftime("%Y-%m-%dT%H:%M:%S")
            else:
                return ''
        else:
            return ''
