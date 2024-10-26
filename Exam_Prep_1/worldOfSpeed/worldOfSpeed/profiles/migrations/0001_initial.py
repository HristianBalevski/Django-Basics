# Generated by Django 5.1.2 on 2024-10-26 10:55

import worldOfSpeed.profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[worldOfSpeed.profiles.validators.validate_username_min_length, worldOfSpeed.profiles.validators.validate_username_allowed_symbols])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(help_text='Age requirement: 21 years and above.', validators=[worldOfSpeed.profiles.validators.validate_minimum_age])),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
