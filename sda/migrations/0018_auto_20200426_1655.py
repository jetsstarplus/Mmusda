# Generated by Django 3.0.3 on 2020-04-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0017_auto_20200426_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaders_department',
            name='Words_From_The_Leader',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='leaders_family',
            name='Words_From_The_Leader',
            field=models.TextField(blank=True),
        ),
    ]
