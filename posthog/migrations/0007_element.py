# Generated by Django 2.2.7 on 2020-01-25 23:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0006_person_distinct_ids"),
    ]

    operations = [
        migrations.CreateModel(
            name="Element",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID",),),
                ("el_text", models.CharField(blank=True, max_length=400, null=True)),
                ("tag_name", models.CharField(blank=True, max_length=400, null=True)),
                ("href", models.CharField(blank=True, max_length=400, null=True)),
                ("attr_id", models.CharField(blank=True, max_length=400, null=True)),
                ("nth_child", models.IntegerField()),
                ("nth_of_type", models.IntegerField()),
                ("attributes", django.contrib.postgres.fields.jsonb.JSONField(default=dict),),
                ("order", models.IntegerField()),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.Event"),),
                ("team", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.Team"),),
            ],
        ),
    ]
