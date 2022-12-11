# Generated by Django 4.1.2 on 2022-10-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figour', '0002_alter_figours_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='fpfigours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('second_price', models.IntegerField()),
                ('Discount', models.IntegerField(blank=True, max_length=2, verbose_name='تخفیف')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
    ]