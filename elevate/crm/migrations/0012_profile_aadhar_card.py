# Generated by Django 5.0.1 on 2024-01-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aadhar_card',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
