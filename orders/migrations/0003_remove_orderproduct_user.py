# Generated by Django 3.1 on 2022-03-12 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
    ]
