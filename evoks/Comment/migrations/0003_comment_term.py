# Generated by Django 3.2.5 on 2021-07-28 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Term', '0002_alter_term_vocabulary'),
        ('Comment', '0002_auto_20210728_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Term.term'),
        ),
    ]
