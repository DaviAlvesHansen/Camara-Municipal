# Generated by Django 5.1.3 on 2025-01-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_rename_year_docs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
