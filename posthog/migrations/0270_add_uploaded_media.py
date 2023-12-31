# Generated by Django 3.2.15 on 2022-10-13 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0269_soft_delete_tiles"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadedMedia",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "media_location",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                (
                    "content_type",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
                ("file_name", models.TextField(blank=True, max_length=1000, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.team"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
