# Generated by Django 3.2.5 on 2021-07-28 15:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabularies', '0009_merge_20210728_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='prefixes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
