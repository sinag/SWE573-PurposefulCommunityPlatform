# Generated by Django 2.2.1 on 2019-11-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_auto_20191107_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='datatype',
        ),
    ]
