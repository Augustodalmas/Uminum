# Generated by Django 5.0.1 on 2024-02-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blocos', '0008_alter_produto_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='pdf',
            field=models.FileField(default='media/pdfs/ola.pdf', upload_to=''),
        ),
    ]
