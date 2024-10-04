# Generated by Django 5.1.1 on 2024-10-03 18:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_completed_task_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expired_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
