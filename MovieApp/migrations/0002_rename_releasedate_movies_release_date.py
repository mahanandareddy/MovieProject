# Generated by Django 4.1.7 on 2023-03-27 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='releasedate',
            new_name='release_date',
        ),
    ]