# Generated by Django 4.0.2 on 2022-07-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutuphane', '0020_remove_atikcodes_atığın adı_atikcodes_atık ismi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atikcodes',
            name='Ait oldugu atık türü',
            field=models.TextField(default='', help_text='örn. Tıbbi atık', max_length=70, null=True),
        ),
    ]
