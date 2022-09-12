# Generated by Django 4.0.5 on 2022-08-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='services')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
