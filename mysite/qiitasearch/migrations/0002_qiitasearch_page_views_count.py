# Generated by Django 3.0.4 on 2022-07-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qiitasearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qiitasearch',
            name='page_views_count',
            field=models.IntegerField(default=0),
        ),
    ]