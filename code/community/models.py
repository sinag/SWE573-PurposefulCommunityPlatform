from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    description = models.CharField(max_length=500, blank=False)
    # ToDo convert post_count to joined table result when posts are available
    post_count = models.BigIntegerField(blank=False, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "communities"
