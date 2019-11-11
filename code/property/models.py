from django.db import models

from datatype.models import DataType
from root import settings


class Property(models.Model):
    datatype = models.ForeignKey(DataType, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    type = models.SmallIntegerField(blank=False,
                                    null=False)  # Todo - document enumeration 0 text, 1 int, 2 datetime 3 enum 4

    # image, 5 audio, 6 video, 7 email, 8 url

    def __str__(self):
        return str(str(self.id) + '-' + self.name)

    class Meta:
        verbose_name = "property"
        verbose_name_plural = "properties"
