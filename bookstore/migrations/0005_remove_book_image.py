# Generated by Django 4.1.1 on 2023-03-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
