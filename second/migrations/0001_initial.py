# Generated by Django 4.0.1 on 2022-03-28 13:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801XXXXXX'. Up to 14 digits allowed.", regex='^(?:\\+88|88)?(01[3-9]\\d{8})$')])),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('Bronze', 'Globalnet Bronze'), ('Silver', 'Globalnet Silver'), ('Gold', 'Globalnet Gold')], default='Bronze', max_length=20)),
                ('dateOfBuy', models.DateField(auto_now=True)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.phone_number')),
            ],
        ),
    ]
