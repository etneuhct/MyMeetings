# Generated by Django 3.1.2 on 2020-10-24 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='group',
            new_name='team',
        ),
    ]
