# Generated by Django 4.0.4 on 2022-05-05 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cleaning_company', '0001_initial'),
        ('service_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('area', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hourse', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cleaning_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_type.service')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaning_company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
