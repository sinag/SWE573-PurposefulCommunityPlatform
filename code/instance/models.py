from django.db import models

from datatype.models import DataType
from root import settings


class Instance(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now_add=True, blank=False,
                                      null=False)  # ToDo - Auto update this on record update
    datatype = models.ForeignKey(DataType, on_delete=models.PROTECT, blank=False, null=False, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "instance"
        verbose_name_plural = "instances"
