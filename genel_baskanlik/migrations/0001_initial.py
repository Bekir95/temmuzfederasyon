# Generated by Django 4.2.1 on 2023-06-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denetim_Kurulu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yonetici_Ismi', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Sifati', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Biyografi', models.TextField(blank=True, null=True)),
                ('Yonetici_Resmi', models.ImageField(blank=True, null=True, upload_to='genel_baskanlik/static/img/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Disiplin_Kurulu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yonetici_Ismi', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Sifati', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Biyografi', models.TextField(blank=True, null=True)),
                ('Yonetici_Resmi', models.ImageField(blank=True, null=True, upload_to='genel_baskanlik/static/img/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Yonetim_Kurulu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yonetici_Ismi', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Sifati', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Biyografi', models.TextField(blank=True, null=True)),
                ('Yonetici_Resmi', models.ImageField(blank=True, null=True, upload_to='genel_baskanlik/static/img/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Yurutme_Kurulu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yonetici_Ismi', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Sifati', models.CharField(blank=True, max_length=100, null=True)),
                ('Yonetici_Biyografi', models.TextField(blank=True, null=True)),
                ('Yonetici_Resmi', models.ImageField(blank=True, null=True, upload_to='genel_baskanlik/static/img/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
