# Generated by Django 4.2.17 on 2025-02-20 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productmodel_brief_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
