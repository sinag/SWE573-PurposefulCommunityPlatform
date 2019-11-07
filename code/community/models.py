from django.contrib.auth.models import User
from django.db import models

from root import settings


class DataType(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    generic = models.BooleanField(db_index=True)  # False = Custom, True = Generic

    def __str__(self):
        return str(str(self.id) + '-' + self.name)

    class Meta:
        verbose_name = "datatype"
        verbose_name_plural = "datatypes"


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


class TextField(models.Model):
    value = models.CharField(max_length=255)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "textfield"
        verbose_name_plural = "textfields"


class IntegerField(models.Model):
    value = models.BigIntegerField()
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, blank=False, null=False, db_index=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "integerfield"
        verbose_name_plural = "integerfields"


class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                               blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    # ToDo convert post_count to joined table result when posts are available
    post_count = models.BigIntegerField(blank=False, null=False, db_index=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "community"
        verbose_name_plural = "communities"
