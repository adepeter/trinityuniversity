# Generated by Django 3.2.8 on 2021-10-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_initial'),
        ('faculties', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='programmes',
            field=models.ManyToManyField(to='academics.Programme'),
        ),
    ]
