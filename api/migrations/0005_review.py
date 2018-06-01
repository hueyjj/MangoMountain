# Generated by Django 2.0.5 on 2018-05-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_sectionlab_course_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(blank=True, max_length=300)),
                ('date_posted', models.CharField(blank=True, max_length=300)),
                ('author', models.CharField(blank=True, max_length=300)),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]