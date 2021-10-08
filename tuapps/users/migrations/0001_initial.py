# Generated by Django 3.2.8 on 2021-10-07 12:21

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import tuapps.users.managers.user
import tuapps.users.models.user
import tuapps.users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('username', models.CharField(db_index=True, max_length=25, unique=True, validators=[tuapps.users.validators.validate_username], verbose_name='username')),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=6, null=True, verbose_name='sex')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=tuapps.users.models.user.upload_to, verbose_name='Profile picture')),
                ('fullname', models.CharField(blank=True, max_length=255, null=True, verbose_name='full name')),
                ('about', models.TextField(blank=True, help_text='Brief description of yourself', verbose_name='About you')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is superuser')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('telephone', models.CharField(blank=True, default='2348097799871', max_length=20, verbose_name='Telephone')),
                ('country', models.CharField(blank=True, choices=[('None', 'Please enter a country')], max_length=4, null=True, verbose_name='Country')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date and time of registration', verbose_name='Registration date')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='Date and time of profile last modification', verbose_name='Last modified')),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time user was last active', verbose_name='Last time seen')),
                ('ip_address', models.GenericIPAddressField(blank=True, help_text='IP Address', null=True, verbose_name='IP Address')),
                ('visits', models.PositiveIntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['email', 'username'],
            },
            managers=[
                ('objects', tuapps.users.managers.user.UserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['id', 'username'], name='idx_user_id_username'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email', 'username'), name='unique_constraint_user_email_username'),
        ),
    ]
