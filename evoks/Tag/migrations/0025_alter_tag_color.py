# Generated by Django 3.2.5 on 2021-08-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0024_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('green', 'Green'), ('pink', 'Pink'), ('yellow', 'Yellow'), ('purple', 'Purple')], default='red', max_length=30),
        ),
    ]
