# Generated by Django 3.2.5 on 2021-07-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
        ('vocabularies', '0003_alter_vocabulary_term_count'),
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='vocabulary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vocabularies.vocabulary'),
        ),
    ]
