# Generated by Django 5.0.6 on 2024-05-26 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('headings', models.TextField(blank=True, null=True)),
                ('paragraphs', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='scraper.url')),
            ],
        ),
    ]
