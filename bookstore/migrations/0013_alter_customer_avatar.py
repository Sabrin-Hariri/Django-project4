# Generated by Django 4.1.1 on 2023-04-11 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_alter_book_file_alter_book_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='preson.png', null=True, upload_to=''),
        ),
    ]