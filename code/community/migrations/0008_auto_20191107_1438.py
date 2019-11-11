# Generated by Django 2.2.1 on 2019-11-07 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0007_delete_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': 'community', 'verbose_name_plural': 'communities'},
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=500)),
                ('author', models.ForeignKey(default=7, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'datatype',
                'verbose_name_plural': 'datatypes',
            },
        ),
        migrations.AddField(
            model_name='community',
            name='datatype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='community.DataType'),
        ),
    ]