# Generated by Django 2.2.1 on 2019-11-25 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0017_auto_20191108_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='post_count',
        ),
    ]