# Generated by Django 2.2.1 on 2020-01-02 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textfield', '0003_auto_20191125_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfield',
            name='value',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
