# Generated by Django 4.1.1 on 2023-03-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='media/img'),
        ),
    ]
