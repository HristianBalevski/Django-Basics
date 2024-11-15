# Generated by Django 5.1.2 on 2024-10-27 07:50

import django.core.validators
import finalExamApp.author.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), finalExamApp.author.validators.check_if_name_is_only_letters])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), finalExamApp.author.validators.check_if_name_is_only_letters])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits', validators=[finalExamApp.author.validators.validate_passcode])),
                ('pets_number', models.PositiveSmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]