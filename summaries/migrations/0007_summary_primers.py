# Generated by Django 3.2.6 on 2021-08-18 14:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0006_remove_summary_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='primers',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), null=True, size=2), blank=True, null=True, size=5),
        ),
    ]