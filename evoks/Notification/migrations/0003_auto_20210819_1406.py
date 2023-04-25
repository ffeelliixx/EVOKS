# Generated by Django 3.2.6 on 2021-08-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0002_notification_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('SUCCESS', 'Success'), ('ERROR', 'Error'), ('WARNING', 'Warning')], default='ERROR', max_length=30),
        ),
    ]
