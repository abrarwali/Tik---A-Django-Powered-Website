# Generated by Django 2.1 on 2018-12-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0005_remove_discussion_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='author',
            field=models.CharField(max_length=15, null=True),
        ),
    ]