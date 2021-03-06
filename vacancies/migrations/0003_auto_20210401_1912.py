# Generated by Django 3.1.6 on 2021-04-01 14:12

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20210401_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(error_messages={'invalid': 'Введите корректный номер телефона. Пример: +7 999 887 33 22'}, max_length=128, region='RU', verbose_name='номер телефона'),
        ),
    ]
