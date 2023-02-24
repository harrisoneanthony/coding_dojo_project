# Generated by Django 2.2.4 on 2023-02-24 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood_events_app', '0003_auto_20230223_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='neighborhood_events_app.User'),
        ),
    ]