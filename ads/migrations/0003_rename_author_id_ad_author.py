# Generated by Django 4.1.1 on 2022-10-04 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
    ]
