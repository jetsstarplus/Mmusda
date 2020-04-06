# Generated by Django 3.0.3 on 2020-04-02 13:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0020_auto_20200402_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 139396, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 140393, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 143385, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 142388, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 139396, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 141390, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 17, 34, 141390, tzinfo=utc), verbose_name='date published')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_leader')),
            ],
        ),
    ]
