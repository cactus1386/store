# Generated by Django 4.1.2 on 2022-11-14 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figourlist', '0003_afirstline_bsecondline_cthirdline_dfourthline_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cThirdLine',
            new_name='firstPage',
        ),
        migrations.DeleteModel(
            name='afirstLine',
        ),
        migrations.DeleteModel(
            name='bSecondLine',
        ),
        migrations.DeleteModel(
            name='dfourthline',
        ),
        migrations.DeleteModel(
            name='eFifthLine',
        ),
        migrations.DeleteModel(
            name='fSixthLine',
        ),
        migrations.DeleteModel(
            name='gseventhLine',
        ),
        migrations.DeleteModel(
            name='heightLine',
        ),
    ]