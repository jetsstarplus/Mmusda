# Generated by Django 3.0.3 on 2020-04-02 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0019_auto_20200402_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcement_classification',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announcement_specification',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 12, 12, 17, 628683, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 12, 12, 17, 629681, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 12, 12, 17, 633670, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 12, 12, 17, 631676, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 12, 12, 17, 628683, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 12, 12, 17, 631676, tzinfo=utc), verbose_name='date published'),
        ),
    ]
