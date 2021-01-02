# Generated by Django 3.1.4 on 2021-01-02 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tweets", "0002_auto_20210102_1043"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="auth.user"
            ),
            preserve_default=False,
        ),
    ]
