# Generated by Django 2.2.2 on 2020-04-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
