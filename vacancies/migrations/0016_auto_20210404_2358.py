# Generated by Django 3.1.6 on 2021-04-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0015_auto_20210404_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_photo',
            field=models.ImageField(blank=True, upload_to='user_images/photo_application', verbose_name='фотография'),
        ),
    ]
