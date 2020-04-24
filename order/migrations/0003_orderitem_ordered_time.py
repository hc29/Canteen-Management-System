# Generated by Django 2.2.2 on 2020-04-21 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ordered_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]