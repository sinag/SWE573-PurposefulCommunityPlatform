from django.db import models

from instance.models import Instance
from property.models import Property


class DateTimeField(models.Model):
    value = models.DateField(blank=True, null=True)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=False, null=False, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "datetimefield"
        verbose_name_plural = "datetimefields"