# Generated by Django 5.1 on 2024-11-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_doctorregistration_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorregistration',
            name='login_status',
            field=models.IntegerField(default=0),
        ),
    ]
