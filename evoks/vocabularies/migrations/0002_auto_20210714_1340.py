# Generated by Django 3.2.5 on 2021-07-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabularies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='description',
            field=models.CharField(default='', max_length=30),
        ),
    ]
