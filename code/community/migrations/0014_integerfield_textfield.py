# Generated by Django 2.2.1 on 2019-11-07 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_auto_20191107_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.Instance')),
            ],
            options={
                'verbose_name': 'textfield',
                'verbose_name_plural': 'textfields',
            },
        ),
        migrations.CreateModel(
            name='IntegerField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField()),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.Instance')),
            ],
            options={
                'verbose_name': 'integerfield',
                'verbose_name_plural': 'integerfields',
            },
        ),
    ]
