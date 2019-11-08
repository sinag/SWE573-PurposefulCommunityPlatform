from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_community_id(context):
    result = 0
    path = str(context['request'].path)
    if path.__contains__('communities'):
        count = len(path.split('/'))
        if count == 4:
            result = path.split('/')[2]
    return result
