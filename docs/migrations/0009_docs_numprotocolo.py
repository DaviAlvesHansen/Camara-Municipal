# Generated by Django 5.1.3 on 2025-01-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0008_alter_docs_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='numProtocolo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
