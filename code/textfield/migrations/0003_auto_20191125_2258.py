# Generated by Django 2.2.1 on 2019-11-25 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textfield', '0002_auto_20191113_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfield',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property'),
        ),
    ]
