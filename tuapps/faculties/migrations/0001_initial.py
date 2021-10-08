# Generated by Django 3.2.8 on 2021-10-07 12:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('termination_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_current', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='noreply@localhost', max_length=254)),
                ('phone', models.CharField(blank=True, default='2348097799871', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Unique URL Identifier', unique=True, verbose_name='URL Identifier')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='noreply@localhost', max_length=254)),
                ('phone', models.CharField(blank=True, default='2348097799871', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.CharField(blank=True, max_length=100)),
                ('long_description', martor.models.MartorField(blank=True, default='No detailed description of faculty yet')),
                ('slug', models.SlugField(help_text='Unique URL Identifier', unique=True, verbose_name='URL Identifier')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FacultyMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('termination_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_current', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headofdepartments', to='faculties.department')),
            ],
        ),
    ]