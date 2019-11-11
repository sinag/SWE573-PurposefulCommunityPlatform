from django.db import models

from instance.models import Instance
from property.models import Property


class TextField(models.Model):
    value = models.CharField(max_length=255)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "textfield"
        verbose_name_plural = "textfields"