# Generated by Django 3.0.7 on 2020-06-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0005_auto_20200630_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='costumer_phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
