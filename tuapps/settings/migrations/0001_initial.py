# Generated by Django 3.2.8 on 2021-10-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Faculty position name', max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Trinity University', help_text='Website title', max_length=20, verbose_name='site title')),
                ('description', models.TextField(blank=True, help_text='Website meta-tag description contents', verbose_name='site description')),
                ('email', models.EmailField(default='noreply@localhost', max_length=254, verbose_name='e-mail')),
                ('welcome_mail', models.TextField(blank=True, help_text='message after successful registration', verbose_name='welcome message')),
                ('is_under_maintenance', models.BooleanField(help_text='Determine if site is under maintenance', null=True, verbose_name='maintenance status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='position',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='unique_name_and_slug'),
        ),
    ]