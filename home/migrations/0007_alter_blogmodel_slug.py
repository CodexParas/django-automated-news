# Generated by Django 4.1.10 on 2023-10-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_blogmodel_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]