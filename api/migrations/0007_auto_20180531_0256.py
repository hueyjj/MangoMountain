# Generated by Django 2.0.5 on 2018-05-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180531_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_posted',
        ),
    ]
