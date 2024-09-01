# Generated by Django 5.0.6 on 2024-05-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('headings', models.TextField(blank=True, null=True)),
                ('paragraphs', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ScrapedContent',
        ),
        migrations.DeleteModel(
            name='URL',
        ),
    ]
