# Generated by Django 5.0.2 on 2024-02-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='enquiry_id',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]