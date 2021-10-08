# Generated by Django 3.2.8 on 2021-10-07 12:21

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tuapps.galleries.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='galleries.folder', verbose_name='root')),
            ],
            options={
                'verbose_name_plural': 'Folders',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=tuapps.galleries.models.upload_to)),
                ('caption', models.CharField(max_length=255)),
                ('is_hidden', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='galleries.folder')),
            ],
            options={
                'verbose_name_plural': 'Media',
                'ordering': ['file'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=tuapps.galleries.models.upload_to)),
                ('caption', models.CharField(max_length=255)),
                ('is_hidden', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='galleries.folder')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'ordering': ['image'],
            },
        ),
    ]