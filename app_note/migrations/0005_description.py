# Generated by Django 4.1.3 on 2022-11-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_note', '0004_remove_topic_topic_big'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]