# Generated by Django 3.0.3 on 2020-04-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0011_auto_20200415_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_category',
            name='department_role',
            field=models.TextField(),
        ),
    ]
