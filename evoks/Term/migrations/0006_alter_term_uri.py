# Generated by Django 3.2.6 on 2021-08-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Term', '0005_alter_term_uri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='uri',
            field=models.CharField(default='', max_length=200),
        ),
    ]
