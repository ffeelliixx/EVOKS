# Generated by Django 3.2.5 on 2021-08-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0020_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('green', 'Green'), ('pink', 'Pink'), ('yellow', 'Yellow'), ('purple', 'Purple')], default='blue', max_length=30),
        ),
    ]