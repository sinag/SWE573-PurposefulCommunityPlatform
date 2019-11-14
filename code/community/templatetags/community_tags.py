from django import template
from community.models import Community
from integerfield.models import IntegerField
from textfield.models import TextField

register = template.Library()


@register.filter
def subscription_id(community_id, user_id):
    return Community.objects.get(id=community_id).subscription_set.all().filter(user__id=user_id)[0].id


@register.filter
def subscription_count_by_user(community_id, user_id):
    return Community.objects.get(id=community_id).subscription_set.all().filter(user__id=user_id).count()


@register.filter
def subscription_count(community_id):
    return Community.objects.get(id=community_id).subscription_set.all().count()


@register.filter
def posttype_count(community_id):
    return Community.objects.get(id=community_id).datatype_set.all().count()


@register.filter
def reference_count(community_id):  # Todo - add post count
    return Community.objects.get(id=community_id).subscription_set.all().count() + Community.objects.get(
        id=community_id).datatype_set.all().count()


@register.filter
def community_owner(community_id):
    return Community.objects.all().get(id=community_id).author


@register.filter
def community_name(community_id):
    return Community.objects.all().get(id=community_id).name


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
