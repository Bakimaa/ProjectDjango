# Generated by Django 5.2 on 2025-05-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jeux',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
    ]
