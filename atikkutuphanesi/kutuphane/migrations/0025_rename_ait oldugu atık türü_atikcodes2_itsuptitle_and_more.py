# Generated by Django 4.0.2 on 2022-07-03 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kutuphane', '0024_rename_atikcodes_atikcodes2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atikcodes2',
            old_name='Ait oldugu atık türü',
            new_name='itsUpTitle',
        ),
        migrations.RenameField(
            model_name='atikcodes2',
            old_name='Atık ismi',
            new_name='wasteName',
        ),
        migrations.RenameField(
            model_name='atikcodes2',
            old_name='Uygun kodu seçiniz',
            new_name='wasteType',
        ),
    ]
