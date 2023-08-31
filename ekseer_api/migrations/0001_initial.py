# Generated by Django 4.2.3 on 2023-08-29 23:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(help_text='Full name should contain only letters.', max_length=255, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Full name should contain only letters.', regex='^[A-Za-z ]+$')])),
                ('iqama_number', models.CharField(help_text='IQAMA number must start with 1 or 2 and be 10 digits long.', max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='IQAMA number must start with 1 or 2 and be 10 digits long.', regex='^[1-2][0-9]{9}$')])),
                ('copy_of_iqama_number', models.ImageField(max_length=512, upload_to='copy_of_iqama_number')),
                ('mobile_number', models.CharField(default='', help_text='The mobile number should start with 5 and be 9 digits long.', max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='The mobile number should start with 5 and be 9 digits long.', regex='^5\\d{8}$')])),
                ('email', models.EmailField(default='', help_text='The email address should be unique and valid.', max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(default='', help_text='The nationality should be a valid country code.', max_length=255)),
                ('password', models.CharField(max_length=128, null=True)),
                ('scfhs_registration', models.CharField(blank=True, max_length=255, null=True)),
                ('copy_of_scfhs_registration_card', models.ImageField(blank=True, max_length=512, null=True, upload_to='copy_of_scfhs_registration_card')),
                ('cv', models.FileField(blank=True, max_length=512, null=True, upload_to='doctors_cv')),
                ('personal_photo', models.ImageField(blank=True, max_length=512, null=True, upload_to='doctors_personal_photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_actived', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('meeting_id', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor_id', models.IntegerField(blank=True, null=True)),
                ('is_new', models.BooleanField(default=True)),
                ('patient_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
