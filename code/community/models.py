from django.contrib.auth.models import User
from django.db import models
from root import settings


class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "community"
        verbose_name_plural = "communities"




