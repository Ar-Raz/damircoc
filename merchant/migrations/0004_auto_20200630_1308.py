# Generated by Django 3.0.7 on 2020-06-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0003_item_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_1',
        ),
        migrations.AddField(
            model_name='order',
            name='costumer_name',
            field=models.CharField(default=True, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='costumer_phone_number',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
