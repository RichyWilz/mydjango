# Generated by Django 4.0.5 on 2022-08-24 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_borrow_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='user',
        ),
    ]
