# Generated by Django 2.1.3 on 2018-11-26 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uchiha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes4',
            name='uploader',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notes4',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='notes4',
            name='subject',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='notes4',
            name='tags',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='notes4',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]