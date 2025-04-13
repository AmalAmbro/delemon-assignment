# Generated by Django 5.2 on 2025-04-13 07:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('views', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_sq_ft', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate_per_sq_ft', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_no', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
