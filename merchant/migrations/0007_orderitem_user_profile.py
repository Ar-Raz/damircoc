# Generated by Django 3.0.7 on 2020-06-30 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0006_auto_20200630_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user_profile',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='merchant.UserProfile'),
            preserve_default=False,
        ),
    ]
