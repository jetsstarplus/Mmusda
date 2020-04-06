# Generated by Django 3.0.3 on 2020-04-02 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0016_auto_20200402_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 11, 34, 12, 277212, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 11, 34, 12, 279208, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 11, 34, 12, 282169, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 11, 34, 12, 280173, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 11, 34, 12, 278217, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 11, 34, 12, 279208, tzinfo=utc), verbose_name='date published'),
        ),
    ]
