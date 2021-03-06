# Generated by Django 3.0.3 on 2020-04-10 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0006_auto_20200410_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='church_member',
            options={'verbose_name_plural': 'Church Members'},
        ),
        migrations.AlterModelOptions(
            name='leaders_department',
            options={'verbose_name_plural': 'Department Leaders'},
        ),
        migrations.AlterModelOptions(
            name='otherbussiness',
            options={'verbose_name_plural': 'Other Businesses'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='visitor_word',
            options={'verbose_name_plural': 'Visitor Word'},
        ),
        migrations.AddField(
            model_name='services',
            name='TimeLIne',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 242280, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 238376, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 240329, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 244265, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 242280, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 239352, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='services',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 240329, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 14, 2, 1, 241304, tzinfo=utc), verbose_name='date published'),
        ),
    ]
