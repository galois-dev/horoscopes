# Generated by Django 4.0 on 2021-12-22 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horoscope',
            options={'ordering': ['-created_at']},
        ),
    ]