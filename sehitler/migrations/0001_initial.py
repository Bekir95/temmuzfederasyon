# Generated by Django 4.2.1 on 2023-06-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sehit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sehit_Ismi', models.CharField(blank=True, max_length=100, null=True)),
                ('Sehit_Meslegi', models.CharField(blank=True, max_length=100, null=True)),
                ('Sehit_Resmi', models.ImageField(blank=True, null=True, upload_to='sehitler/static/img/')),
            ],
        ),
    ]