# Generated by Django 3.1.6 on 2021-04-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0016_auto_20210404_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_photo',
            field=models.ImageField(blank=True, default=None, upload_to='user_images/photo_application', verbose_name='фотография'),
        ),
    ]
