# Generated by Django 3.1.4 on 2020-12-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=True, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(),
        ),
    ]
