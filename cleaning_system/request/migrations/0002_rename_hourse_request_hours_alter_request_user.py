# Generated by Django 4.0.4 on 2022-05-12 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='hourse',
            new_name='hours',
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
