# Generated by Django 3.0.3 on 2020-04-07 13:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0022_auto_20200403_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsdetail',
            old_name='event_id',
            new_name='event',
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 671529, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 669535, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_link',
            field=models.ImageField(upload_to='sda'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 670530, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 673522, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 672529, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 669535, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 13, 59, 29, 671529, tzinfo=utc), verbose_name='date published'),
        ),
    ]
