# Generated by Django 2.1 on 2018-10-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20181001_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(default='', max_length=31),
        ),
    ]