# Generated by Django 4.1 on 2022-09-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trustee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='trustee/')),
                ('name', models.CharField(max_length=100)),
                ('Native', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
