# Generated by Django 2.0.1 on 2018-03-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180313_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='meeting', to='meeting.Meeting'),
        ),
    ]
