# Generated by Django 4.1.5 on 2023-02-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_phrases_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrases',
            name='image_url',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
