# Generated by Django 5.2.4 on 2025-07-29 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0002_category_parent_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
