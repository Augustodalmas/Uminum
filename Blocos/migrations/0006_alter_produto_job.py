# Generated by Django 5.0.1 on 2024-02-15 15:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blocos', '0005_alter_produto_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='Job',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')]),
        ),
    ]
