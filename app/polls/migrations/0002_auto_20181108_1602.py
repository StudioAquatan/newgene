# Generated by Django 2.1 on 2018-11-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilemessage',
            name='lat',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='mobilemessage',
            name='lng',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='servermessage',
            name='lat',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='servermessage',
            name='lng',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
    ]
