# Generated by Django 4.1.1 on 2023-04-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0015_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='book2.png', null=True, upload_to=''),
        ),
    ]