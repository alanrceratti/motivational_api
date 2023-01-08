# Generated by Django 4.1.5 on 2023-01-08 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phrases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phrase', models.CharField(max_length=255, unique=True, verbose_name='Phrase')),
                ('image', models.ImageField(upload_to='media/')),
                ('image_url', models.CharField(max_length=255)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phrases', to='api.category')),
            ],
            options={
                'verbose_name': 'Phrase',
                'verbose_name_plural': 'Phrases',
            },
        ),
    ]
