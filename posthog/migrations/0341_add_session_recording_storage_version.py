# Generated by Django 3.2.19 on 2023-08-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0340_action_bytecode"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionrecording",
            name="storage_version",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
