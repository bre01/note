# Generated by Django 4.1.3 on 2022-11-21 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='topic_name',
        ),
    ]
