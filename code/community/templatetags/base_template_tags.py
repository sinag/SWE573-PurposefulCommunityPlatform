from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_community_community_id(context):
    result = 0
    path = str(context['request'].path)
    if path.__contains__('communities') and not path.__contains__('update') and not path.__contains__(
            'delete') and not path.__contains__('creat'):
        count = len(path.split('/'))
        if count == 4:
            result = path.split('/')[2]
    return result


@register.simple_tag(takes_context=True)
def get_datatype_community_id(context):
    result = 0
    path = str(context['request'].path)
    if path.__contains__('datatypes') and not path.__contains__('update') and not path.__contains__(
            'delete') and not path.__contains__('create'):
        count = len(path.split('/'))
        if count == 3:
            result = path.split('/')[2]
    return result
