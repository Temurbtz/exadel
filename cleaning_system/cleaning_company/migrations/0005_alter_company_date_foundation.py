# Generated by Django 4.0.4 on 2022-05-11 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_company', '0004_alter_company_date_foundation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date_foundation',
            field=models.DateField(default=datetime.datetime(2022, 5, 11, 14, 48, 26, 418766, tzinfo=utc)),
        ),
    ]