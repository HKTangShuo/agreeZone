# Generated by Django 2.1.8 on 2021-10-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20211005_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreebook',
            name='cover',
            field=models.FileField(max_length=128, upload_to='', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='agreebook',
            name='url',
            field=models.FileField(max_length=128, upload_to='', verbose_name='书'),
        ),
    ]