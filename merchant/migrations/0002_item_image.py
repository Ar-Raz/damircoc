# Generated by Django 3.0.7 on 2020-06-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
    ]
