# Generated by Django 2.1.11 on 2019-12-11 22:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Speech2textAnnotation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("prob", models.FloatField(default=0.0)),
                ("manual", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField()),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="speech2text_annotations",
                        to="api.Document",
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Speech2textProject",
            fields=[
                (
                    "project_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.Project",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("api.project",),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("DocumentClassification", "document classification"),
                    ("SequenceLabeling", "sequence labeling"),
                    ("Seq2seq", "sequence to sequence"),
                    ("Speech2text", "speech to text"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="speech2textannotation",
            unique_together={("document", "user")},
        ),
    ]
