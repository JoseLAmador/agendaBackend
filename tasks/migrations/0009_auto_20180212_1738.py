# Generated by Django 2.0.1 on 2018-02-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20180212_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expiry',
            field=models.DateTimeField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='starts',
            field=models.DateTimeField(blank=True, db_index=True),
        ),
    ]