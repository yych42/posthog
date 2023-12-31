# Generated by Django 3.2.5 on 2022-02-17 18:11

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0212_alter_persondistinctid_team"),
    ]

    operations = [
        migrations.RenameField(model_name="dashboard", old_name="tags", new_name="deprecated_tags"),
        migrations.RenameField(model_name="insight", old_name="tags", new_name="deprecated_tags"),
        migrations.AlterField(
            model_name="dashboard",
            name="deprecated_tags",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="insight",
            name="deprecated_tags",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
        migrations.RemoveConstraint(
            model_name="taggeditem",
            name="exactly_one_related_object",
        ),
        migrations.AddField(
            model_name="taggeditem",
            name="dashboard",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tagged_items",
                to="posthog.dashboard",
            ),
        ),
        migrations.AddField(
            model_name="taggeditem",
            name="event_definition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tagged_items",
                to="posthog.eventdefinition",
            ),
        ),
        migrations.AddField(
            model_name="taggeditem",
            name="insight",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tagged_items",
                to="posthog.insight",
            ),
        ),
        migrations.AddField(
            model_name="taggeditem",
            name="property_definition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tagged_items",
                to="posthog.propertydefinition",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="taggeditem",
            unique_together={
                (
                    "tag",
                    "dashboard",
                    "insight",
                    "event_definition",
                    "property_definition",
                    "action",
                )
            },
        ),
        migrations.AddConstraint(
            model_name="taggeditem",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("dashboard__isnull", False),
                        ("insight__isnull", True),
                        ("event_definition__isnull", True),
                        ("property_definition__isnull", True),
                        ("action__isnull", True),
                    ),
                    models.Q(
                        ("dashboard__isnull", True),
                        ("insight__isnull", False),
                        ("event_definition__isnull", True),
                        ("property_definition__isnull", True),
                        ("action__isnull", True),
                    ),
                    models.Q(
                        ("dashboard__isnull", True),
                        ("insight__isnull", True),
                        ("event_definition__isnull", False),
                        ("property_definition__isnull", True),
                        ("action__isnull", True),
                    ),
                    models.Q(
                        ("dashboard__isnull", True),
                        ("insight__isnull", True),
                        ("event_definition__isnull", True),
                        ("property_definition__isnull", False),
                        ("action__isnull", True),
                    ),
                    models.Q(
                        ("dashboard__isnull", True),
                        ("insight__isnull", True),
                        ("event_definition__isnull", True),
                        ("property_definition__isnull", True),
                        ("action__isnull", False),
                    ),
                    _connector="OR",
                ),
                name="exactly_one_related_object",
            ),
        ),
    ]
