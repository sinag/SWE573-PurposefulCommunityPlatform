# Generated by Django 2.2.1 on 2019-11-05 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_auto_20191103_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='author',
            field=models.ForeignKey(default=settings.DEFAULT_ADMIN, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]