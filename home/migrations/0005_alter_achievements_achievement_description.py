# Generated by Django 4.1.1 on 2022-10-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_achievements_achievements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='achievement_description',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
