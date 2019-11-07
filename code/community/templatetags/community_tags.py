from django import template
from community.models import Community

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
def community_owner(community_id):
    return Community.objects.all().get(id=community_id).author
