# Generated by Django 3.1.6 on 2021-04-03 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0008_auto_20210403_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['id'], 'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
    ]
