# Generated by Django 4.1.3 on 2022-11-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_note', '0002_rename_text_topic_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_big',
            field=models.EmailField(default='127.1', max_length=254),
            preserve_default=False,
        ),
    ]
