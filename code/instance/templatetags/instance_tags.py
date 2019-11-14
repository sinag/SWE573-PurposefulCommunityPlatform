from django import template
from datatype.models import DataType
from instance.models import Instance
from integerfield.models import IntegerField
from textfield.models import TextField

register = template.Library()


@register.simple_tag
def datatype_fields(datatype_id):
    return DataType.objects.get(id=datatype_id).fields


@register.simple_tag
def datatype_fields_from_instance_id(instance_id):
    return Instance.objects.get(id=instance_id).datatype.fields


@register.filter
def datatype_name(datatype_id):
    return DataType.objects.get(id=datatype_id).name


@register.filter
def datatype_name_from_instance_id(instance_id):
    return Instance.objects.get(id=instance_id).datatype.name


# Todo - this tag also exists in community_tags, think about merge
@register.simple_tag
def property_value(instance_id, property_id, property_type):
    if property_type == 0:  # Todo - add other datatype support
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
