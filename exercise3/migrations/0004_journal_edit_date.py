# Generated by Django 2.0.13 on 2019-06-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise3', '0003_auto_20190621_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
