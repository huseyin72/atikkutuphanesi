# Generated by Django 4.0.2 on 2022-07-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutuphane', '0025_rename_ait oldugu atık türü_atikcodes2_itsuptitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttonpart',
            name='olusabilecek_digerId',
            field=models.TextField(default='', help_text='aralarında nokta olacak şekilde örn 34.553.', max_length=1000),
        ),
        migrations.AddField(
            model_name='buttonpart',
            name='proseskaynakliId',
            field=models.TextField(default='', help_text='aralarında nokta olacak şekilde örn 34.553.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='buttonpart',
            name='olusabilecek_diger',
            field=models.TextField(default='', help_text='aralarında nokta olacak sekilde ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='buttonpart',
            name='prosesKaynakli',
            field=models.TextField(default='', help_text='aralarında nokta olacak sekilde ', max_length=1000),
        ),
    ]