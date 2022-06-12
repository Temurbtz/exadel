# Generated by Django 4.0.5 on 2022-06-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_notification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.IntegerField(choices=[(1, 'Read'), (0, 'Not Read')], default=0),
        ),
    ]
