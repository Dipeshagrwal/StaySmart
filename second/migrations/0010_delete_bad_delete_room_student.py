# Generated by Django 4.1 on 2022-10-08 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0009_delete_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bad',
        ),
        migrations.DeleteModel(
            name='room_student',
        ),
    ]
