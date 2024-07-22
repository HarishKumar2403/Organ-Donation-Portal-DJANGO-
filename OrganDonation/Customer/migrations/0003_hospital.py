# Generated by Django 4.0.3 on 2024-03-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_donationform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]
