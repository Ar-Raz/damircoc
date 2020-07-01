# Generated by Django 3.0.7 on 2020-07-01 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merchant', '0009_orderitem_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='costumer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='costumer_phone_number',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.CreateModel(
            name='CostumerUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costumer_name', models.CharField(max_length=64)),
                ('costumer_phone_number', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='costumer',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='merchant.CostumerUserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='costumer',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='merchant.CostumerUserProfile'),
            preserve_default=False,
        ),
    ]
