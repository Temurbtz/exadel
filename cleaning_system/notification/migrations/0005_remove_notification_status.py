# Generated by Django 4.0.5 on 2022-06-09 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_alter_notification_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='status',
        ),
    ]