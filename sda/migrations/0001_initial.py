# Generated by Django 3.0.3 on 2020-04-08 13:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Church_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=20)),
                ('Adm_Year', models.IntegerField(verbose_name='Year Of Admission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=20)),
                ('department_role', models.CharField(max_length=500)),
                ('department_inspiration', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, choices=[('Members Welfare', 'Members Welfare'), ('Internal Activities', 'Internal Activities'), ('Church Affairs', 'Church Affairs'), ('Ministry & Outreach', 'Ministry & Outreach')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField(verbose_name='Due Date')),
                ('description', models.TextField()),
                ('image_link', models.ImageField(upload_to='sda')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 756883, tzinfo=utc), verbose_name='Publication Date')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(choices=[('Emeralds', 'Emeralds'), ('Heralds', 'Heralds'), ('Humble', 'Humble'), ('Aroma', 'Aroma'), ('Pilgrims', 'Pilgrims'), ('Royals', 'Royals'), ('Eagles', 'Eagles'), ('All', 'All')], max_length=20)),
                ('inspiration', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 760872, tzinfo=utc), verbose_name='Date Published')),
            ],
        ),
        migrations.CreateModel(
            name='visitor_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 757880, tzinfo=utc), verbose_name='date published')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='Scripture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scripture_title', models.CharField(max_length=30)),
                ('scripture_content', models.TextField()),
                ('attached_verses', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 756883, tzinfo=utc), verbose_name='Date published')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='OtherBussiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_title', models.CharField(max_length=30)),
                ('other_description', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 758877, tzinfo=utc), verbose_name='Date Published')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='Leaders_Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam_role', models.CharField(choices=[('mom', 'Family Mom'), ('dad', 'Family Dad'), ('Child', 'Child')], default='Child', max_length=30)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Family')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='Leaders_Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpt_role', models.CharField(choices=[('hod', 'Head Of Department'), ('hod1', 'Assistant Head'), ('hod2', 'Second Assistant'), ('hod3', 'Third Assistant')], default='Family', max_length=30)),
                ('dpt_rate', models.IntegerField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Department')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='EventsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='family_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Family'),
        ),
        migrations.CreateModel(
            name='elder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty', models.BooleanField(verbose_name='Is Elder On Duty')),
                ('short_sharing', models.TextField()),
                ('is_working', models.BooleanField(verbose_name='Is Elder Active')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_title', models.CharField(max_length=30)),
                ('announcement_description', models.TextField()),
                ('announcement_due_date', models.DateTimeField(verbose_name='Due Date')),
                ('publication_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 755885, tzinfo=utc), verbose_name='Date Published')),
                ('announcement_classification', models.CharField(choices=[('Announcement', 'Announcement'), ('Sub-Announcement', 'Sub-Announcement')], max_length=30)),
                ('announcement_specification', models.CharField(default='None', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 8, 13, 35, 36, 758877, tzinfo=utc), verbose_name='date published')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sda.Church_Member')),
            ],
        ),
    ]
