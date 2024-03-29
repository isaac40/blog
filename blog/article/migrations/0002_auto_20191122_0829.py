# Generated by Django 2.2.6 on 2019-11-22 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pubDateTime']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pubDateTime']},
        ),
        migrations.AddField(
            model_name='article',
            name='pubDateTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='pubDateTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
