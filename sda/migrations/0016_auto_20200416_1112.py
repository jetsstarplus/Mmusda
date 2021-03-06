# Generated by Django 3.0.3 on 2020-04-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0015_auto_20200415_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='church_member',
            options={'verbose_name': 'Church Member', 'verbose_name_plural': 'Church Members'},
        ),
        migrations.AlterModelOptions(
            name='leaders_department',
            options={'verbose_name': "Department's Leader", 'verbose_name_plural': "Departments' Leaders"},
        ),
        migrations.AlterModelOptions(
            name='leaders_family',
            options={'verbose_name': "Leader's Family", 'verbose_name_plural': "Leaders' Family"},
        ),
        migrations.AlterModelOptions(
            name='sermons',
            options={'verbose_name': 'Sermon Post', 'verbose_name_plural': 'Sermon Posts'},
        ),
        
        migrations.AddField(
            model_name='family',
            name='family_profile',
            field=models.ImageField(blank=True, upload_to='family_profile'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_category',
            field=models.CharField(blank=True, choices=[('Members Welfare', 'Members Welfare'), ('Internal Activities', 'Internal Activities'), ('Church Affairs', 'Church Affairs'), ('Ministry & Outreach', 'Ministry & Outreach')], max_length=50),
        ),
    ]
