# Generated by Django 4.0.5 on 2022-06-09 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_company_operation_area_delete_city'),
        ('notification', '0002_notification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]