# Generated by Django 5.0.1 on 2024-01-30 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blocos', '0002_produto_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('formato', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='formatoBloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='formasBlocos', to='Blocos.formato'),
        ),
    ]
