# Generated by Django 4.2.7 on 2024-03-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='Corrigido',
            field=models.CharField(choices=[('AUG', 'Augusto'), ('ALE', 'Alessandro'), ('GUI', 'Guilherme'), ('GUS', 'Gustavo')], max_length=12),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='Responsavel',
            field=models.CharField(choices=[('AUG', 'Augusto'), ('ALE', 'Alessandro'), ('GUI', 'Guilherme'), ('GUS', 'Gustavo')], max_length=12),
        ),
    ]
