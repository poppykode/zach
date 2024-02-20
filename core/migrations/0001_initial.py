# Generated by Django 5.0.2 on 2024-02-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_top', models.CharField(max_length=255)),
                ('header_bottom', models.CharField(max_length=255)),
                ('button_link', models.URLField()),
                ('button_text', models.CharField(max_length=50)),
                ('banner_image', models.ImageField(upload_to='banners')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
