# Generated by Django 5.1.3 on 2024-11-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymstore', '0002_order_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
