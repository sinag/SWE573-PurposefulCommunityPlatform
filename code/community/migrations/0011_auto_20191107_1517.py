# Generated by Django 2.2.1 on 2019-11-07 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_auto_20191107_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='datatype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.DataType'),
        ),
    ]