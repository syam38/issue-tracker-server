# Generated by Django 2.1.2 on 2018-10-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]