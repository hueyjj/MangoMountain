# Generated by Django 2.0.5 on 2018-05-20 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180517_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionlab',
            name='sectionlab',
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='class_id',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='enrollment',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='instructor',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='location',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='status',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='time',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='sectionlab',
            name='wait',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AlterField(
            model_name='course',
            name='section_and_labs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.SectionLab'),
        ),
    ]
