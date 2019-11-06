from django.db import models

from community.models import Community
from root import settings


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    community = models.ForeignKey(Community, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "subscriptions"
