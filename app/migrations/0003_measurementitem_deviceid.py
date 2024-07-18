# Generated by Django 5.0.1 on 2024-02-23 08:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_adddevices_device_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurementitem',
            name='deviceId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
