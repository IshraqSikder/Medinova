# Generated by Django 5.0.1 on 2024-03-27 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_types',
            new_name='appointment_type',
        ),
    ]
