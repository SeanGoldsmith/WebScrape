# Generated by Django 2.1.5 on 2019-02-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_blogpost_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
