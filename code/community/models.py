from django.contrib.auth.models import User
from django.db import models

from root import settings


class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.CharField(max_length=500, blank=False)
    # ToDo convert post_count to joined table result when posts are available
    post_count = models.BigIntegerField(blank=False, db_index=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "community"
        verbose_name_plural = "communities"
