# Generated by Django 3.1.3 on 2021-01-04 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20210104_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]