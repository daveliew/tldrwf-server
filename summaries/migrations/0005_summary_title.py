# Generated by Django 3.2.6 on 2021-08-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0004_auto_20210813_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
