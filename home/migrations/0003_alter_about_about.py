# Generated by Django 4.1.1 on 2022-10-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_about_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about',
            field=models.TextField(max_length=10000),
        ),
    ]
