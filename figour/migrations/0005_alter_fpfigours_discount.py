# Generated by Django 4.1.2 on 2022-10-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figour', '0004_alter_fpfigours_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpfigours',
            name='Discount',
            field=models.IntegerField(blank=True, verbose_name='تخفیف'),
        ),
    ]
