from django.db import models

from datatype.models import DataType


class Property(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    type = models.SmallIntegerField(blank=False, null=False,
                                    db_index=True)  # 0 = Text, 1 = Integer, 2 = Datetime, 3 = Enumeration
    datatype = models.ForeignKey(DataType, on_delete=models.PROTECT, blank=False, null=False, db_index=True)

    def __str__(self):
        return str(str(self.id) + '-' + self.name)

    class Meta:
        verbose_name = "property"
        verbose_name_plural = "properties"
