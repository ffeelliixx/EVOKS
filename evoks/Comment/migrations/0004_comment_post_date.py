# Generated by Django 3.2.5 on 2021-07-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0003_comment_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_date',
            field=models.CharField(default='', max_length=126),
        ),
    ]