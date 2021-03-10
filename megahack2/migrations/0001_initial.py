# Generated by Django 3.1.7 on 2021-03-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('query', models.CharField(max_length=500)),
                ('mobile_number', models.BigIntegerField(null=True)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'contactForm',
                'verbose_name_plural': 'contactForms',
            },
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/img/gallery')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='media/img/speaker')),
                ('email_id', models.CharField(max_length=200, null=True)),
                ('instagram_id', models.CharField(max_length=200, null=True)),
                ('linkedIn_id', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'speaker',
                'verbose_name_plural': 'speakers',
            },
        ),
        migrations.CreateModel(
            name='sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='media/img/sponsor')),
                ('website_link', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
        migrations.CreateModel(
            name='youtube_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'youtube_link',
                'verbose_name_plural': 'youtube_links',
            },
        ),
    ]
