# Generated by Django 3.0.4 on 2022-07-08 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gourmet', '0004_auto_20220708_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gourmet',
            name='non_smoking',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gourmet',
            name='wifi',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
