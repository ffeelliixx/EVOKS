# Generated by Django 3.2.6 on 2021-08-22 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GroupProfile', '0005_rename_group_owner1_groupprofile_group_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofile',
            name='group_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
