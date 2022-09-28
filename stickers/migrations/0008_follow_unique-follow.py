# Generated by Django 4.0 on 2022-09-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0007_rename_name_sticker_title_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following_user', 'followed_user'), name='unique-follow'),
        ),
    ]