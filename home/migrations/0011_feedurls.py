# Generated by Django 4.1.10 on 2023-10-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_blogmodel_source_url_blogmodel_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_url', models.CharField(max_length=1000, unique=True)),
            ],
        ),
    ]