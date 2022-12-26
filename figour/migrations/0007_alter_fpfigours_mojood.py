# Generated by Django 4.1.2 on 2022-10-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figour', '0006_fpfigours_mojood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpfigours',
            name='mojood',
            field=models.CharField(choices=[('ناموجود است', 'ناموجود'), ('موجود است', 'موجود')], default='M', max_length=20, verbose_name='موجودی'),
        ),
    ]
