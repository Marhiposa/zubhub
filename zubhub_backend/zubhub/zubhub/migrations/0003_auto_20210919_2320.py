# Generated by Django 2.2.7 on 2021-09-19 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zubhub', '0002_auto_20210919_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='explore_ideas_url',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='footer_logo',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='footer_logo_url',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='header_logo',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='header_logo_url',
        ),
    ]