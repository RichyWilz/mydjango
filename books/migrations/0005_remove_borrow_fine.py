# Generated by Django 4.0.5 on 2022-08-24 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_cover_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='fine',
        ),
    ]
