# Generated by Django 2.2.2 on 2020-04-20 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('details', models.TextField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, default=29, max_digits=4)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date of adding')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
