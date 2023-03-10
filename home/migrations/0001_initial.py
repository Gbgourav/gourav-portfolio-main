# Generated by Django 4.1.1 on 2022-10-10 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievements', models.TextField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default=None, null=True)),
                ('university_name', models.CharField(max_length=200)),
                ('cgpa', models.FloatField(blank=True, default=None, null=True)),
                ('cgpa_outOf', models.IntegerField(blank=True, default=None, null=True)),
                ('percentage', models.FloatField(blank=True, default=None, null=True)),
                ('percentage_outOf', models.IntegerField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='formData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(max_length=5000)),
                ('link', models.CharField(max_length=65535)),
                ('link_name', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('link_report', models.TextField(blank=True, default=None, max_length=65535, null=True)),
                ('link_report_name', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('company_name', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('short_details', models.TextField(blank=True, default=None, null=True)),
                ('skills', models.TextField()),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBasicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('bio', models.TextField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('other_skills', models.TextField()),
                ('profile_image', models.ImageField(blank=True, default=None, null=True, upload_to='profile/')),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='home.languages')),
                ('technical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technical', to='home.technicalskills')),
            ],
        ),
    ]
