# Generated by Django 3.2.16 on 2023-02-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0302_add_user_pending_email_and_is_verified"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="session_recording_version",
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
