# Generated by Django 4.1.6 on 2023-02-10 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CNjokes', '0003_cnjoke_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cnjoke',
            old_name='likes',
            new_name='number_of_likes',
        ),
    ]
