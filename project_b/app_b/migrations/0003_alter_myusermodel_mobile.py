# Generated by Django 5.0.2 on 2024-02-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_b', '0002_alter_myusermodel_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusermodel',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
