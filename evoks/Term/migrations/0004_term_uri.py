# Generated by Django 3.2.6 on 2021-08-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Term', '0003_alter_term_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='uri',
            field=models.CharField(default='', max_length=200),
        ),
    ]
