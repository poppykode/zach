# Generated by Django 5.0.2 on 2024-02-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post_type', models.CharField(choices=[('blog post', 'blog post'), ('news', 'news')], default='blog post', max_length=50)),
                ('author', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('cover_image', models.ImageField(upload_to='blog/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
